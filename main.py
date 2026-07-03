from fastapi import FastAPI, Depends, HTTPException, Header
from sqlalchemy.orm import Session

from database import engine, Base, get_db
from models import Users, Notes
from schemas import UserCreate, UserLogin, NoteCreate, NoteResponse
from auth import *

Base.metadata.create_all(bind=engine)

app = FastAPI(title="Cloud Notes API")

# register
@app.post("/register")
def register(user: UserCreate, db: Session = Depends(get_db)):

    existing = db.query(Users).filter(
        Users.email == user.email
    ).first()

    if existing:
        raise HTTPException(400, "Email already registered")

    new_user = Users(
        name=user.name,
        email=user.email,
        password=hash_password(user.password)
    )

    db.add(new_user)
    db.commit()

    return {"message": "User Registered Successfully"}


# Login
@app.post("/login")
def login(user: UserLogin, db: Session = Depends(get_db)):

    db_user = db.query(Users).filter(
        Users.email == user.email
    ).first()

    if not db_user:
        raise HTTPException(401, "Invalid Credentials")

    if not verify_password(
        user.password,
        db_user.password
    ):
        raise HTTPException(401, "Invalid Credentials")

    token = create_access_token(
        {"user_id": db_user.id}
    )

    return {
        "access_token": token
        }
    
    
# function to get current user
def get_current_user(
    payload=Depends(verify_token),
    db: Session = Depends(get_db)
):

    user = db.query(Users).filter(
        Users.id == payload["user_id"]
    ).first()

    if user is None:
        raise HTTPException(
            status_code=401,
            detail="User not found"
        )

    return user

# create notes
@app.post("/notes")
def create_note(note: NoteCreate, db: Session = Depends(get_db), current_user: Users = Depends(get_current_user)):

    new_note = Notes(
        title=note.title,
        content=note.content,
        owner_id=current_user.id
    )

    db.add(new_note)
    db.commit()

    return {"message": "Note Created Successfully"}


# view notes
@app.get("/notes", response_model=list[NoteResponse]
)
def get_notes(
    db: Session = Depends(get_db),
    current_user: Users = Depends(get_current_user)
):

    return db.query(Notes).filter(
        Notes.owner_id == current_user.id
    ).all()
    

# update notes 
@app.put("/notes/{note_id}")
def update_note(note_id: int, note: NoteCreate, db: Session = Depends(get_db), current_user: Users = Depends(get_current_user)):

    db_note = db.query(Notes).filter(
        Notes.id == note_id,
        Notes.owner_id == current_user.id
    ).first()

    if not db_note:
        raise HTTPException(404, "Note Not Found")

    db_note.title = note.title
    db_note.content = note.content

    db.commit()

    return {"message": "Updated Successfully"}


# Delete note
@app.delete("/notes/{note_id}")
def delete_note(
    note_id: int,
    db: Session = Depends(get_db),
    current_user: Users = Depends(get_current_user)
):

    db_note = db.query(Notes).filter(
        Notes.id == note_id,
        Notes.owner_id == current_user.id
    ).first()

    if not db_note:
        raise HTTPException(404, "Note Not Found")

    db.delete(db_note)
    db.commit()

    return {"message": "Deleted Successfully"}