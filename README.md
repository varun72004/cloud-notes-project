# ☁️ Cloud Notes API

A secure, cloud-based REST API for managing personal notes, built with **FastAPI**, **PostgreSQL**, and **JWT Authentication**. The application is deployed on **Render** and uses **Neon PostgreSQL** as the cloud database.

---

## 🚀 Live Demo

- 🌐 **Live API:** https://cloud-notes-project-r72e.onrender.com
- 📘 **Swagger Documentation:** https://cloud-notes-project-r72e.onrender.com/docs
- 💻 **GitHub Repository:** https://github.com/varun72004/cloud-notes-project

---

# 📖 Project Overview

Cloud Notes API is a backend application that enables users to securely manage their personal notes through RESTful APIs.

Each user can:

- Register a new account
- Login securely
- Receive a JWT Access Token
- Create personal notes
- View only their own notes
- Update their notes
- Delete their notes

The project demonstrates modern backend development practices including secure authentication, cloud databases, ORM relationships, and cloud deployment.

---

# ✨ Features

✅ User Registration

✅ User Login

✅ JWT Authentication

✅ Password Hashing (Bcrypt)

✅ Create Notes

✅ View Notes

✅ Update Notes

✅ Delete Notes

✅ PostgreSQL Cloud Database

✅ SQLAlchemy ORM

✅ Environment Variable Configuration

✅ Interactive Swagger API Documentation

✅ Cloud Deployment on Render

---

# 🛠 Tech Stack

| Technology | Purpose |
|------------|---------|
| Python | Programming Language |
| FastAPI | Backend Framework |
| SQLAlchemy | ORM |
| PostgreSQL | Database |
| Neon | Cloud PostgreSQL |
| JWT | Authentication |
| Passlib (Bcrypt) | Password Hashing |
| Uvicorn | ASGI Server |
| Render | Cloud Deployment |
| Git & GitHub | Version Control |

---

# 📂 Project Structure

```
cloud_notes/
│── main.py
│── auth.py
│── database.py
│── models.py
│── schemas.py
│── requirements.txt
│── .env
│── README.md
```

---

# 🔐 Authentication Flow

```
User Register
        │
        ▼
Password Hashed using Bcrypt
        │
        ▼
Stored in PostgreSQL
        │
        ▼
User Login
        │
        ▼
JWT Token Generated
        │
        ▼
Protected API Access
```

---

# 📌 API Endpoints

## Authentication

| Method | Endpoint | Description |
|---------|----------|-------------|
| POST | `/register` | Register a new user |
| POST | `/login` | Login and receive JWT Token |

---

## Notes

| Method | Endpoint | Description |
|---------|----------|-------------|
| POST | `/notes` | Create Note |
| GET | `/notes` | View User Notes |
| PUT | `/notes/{note_id}` | Update Note |
| DELETE | `/notes/{note_id}` | Delete Note |

---

# ⚙️ Installation

## Clone Repository

```bash
git clone https://github.com/varun72004/cloud-notes-project.git

cd cloud-notes-api
```

---

## Create Virtual Environment

### Windows

```bash
python -m venv venv

venv\Scripts\activate
```

### Linux / Mac

```bash
python3 -m venv venv

source venv/bin/activate
```

---

## Install Dependencies

```bash
pip install -r requirements.txt
```

---

## Configure Environment Variables

Create a `.env` file.

```env
DATABASE_URL=your_database_url

SECRET_KEY=your_secret_key

ALGORITHM=HS256

ACCESS_TOKEN_EXPIRE_MINUTES=60
```

---

## Run the Project

```bash
uvicorn main:app --reload
```

Open

```
https://cloud-notes-project-r72e.onrender.com/```

---

# ☁️ Deployment

This project is deployed using:

- Render (Backend Hosting)
- Neon PostgreSQL (Cloud Database)
- GitHub (Version Control)

---

# 🧪 Testing

The API can be tested using:

- FastAPI Swagger UI
- Postman
- Thunder Client

---

# 📸 Screenshots

## Swagger Documentation

![alt text](<images/Screenshot 2026-07-04 165735.png>)

---

## User Registration

![alt text](<images/Screenshot 2026-07-04 165558.png>)

---

## Login

![alt text](<images/Screenshot 2026-07-04 165158.png>)

---

## Create Note

![alt text](<images/Screenshot 2026-07-04 165016.png>)

---

## View Notes

![alt text](<images/Screenshot 2026-07-04 164743.png>)
---

## Neon Database

![alt text](<images/Screenshot 2026-07-04 164051.png>)

---

# 🔒 Security Features

- JWT Authentication
- Password Hashing using Bcrypt
- Protected Endpoints
- Environment Variables
- Secure PostgreSQL Connection
- User-specific Note Access

---

# 📚 What I Learned

Through this project, I gained hands-on experience with:

- REST API Development
- FastAPI
- SQLAlchemy ORM
- PostgreSQL
- JWT Authentication
- Password Security
- Database Relationships
- Cloud Deployment
- Environment Variables
- Git & GitHub Workflow

---

# 🚀 Future Improvements

- Email Verification
- Password Reset
- Pagination
- Search Notes
- Categories
- File Attachments
- Docker Support
- Unit Testing
- CI/CD Pipeline
- Role-Based Authorization

---

# 👨‍💻 Author

**Varun Sharma**

B.Tech Computer Science Engineering

Aspiring AI/ML & Backend Developer

GitHub:
https://github.com/varun72004

LinkedIn:
www.linkedin.com/in/varun-sharma-4525b1343
---

# ⭐ Support

If you found this project useful, please consider giving it a ⭐ on GitHub.

It helps motivate me to build and share more open-source projects.

---

## 📄 License

This project is licensed under the MIT License.