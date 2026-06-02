1# PROJECT
LOST AND FOUND PROJECT

🎓 Student Community Portal – FastAPI Project

This is a full-stack backend API for a Student Community Portal developed using FastAPI. The portal includes modules for user authentication, announcements, and a lost & found system.


---

🚀 Features

👤 User Authentication

Registration with password strength validation

Secure password hashing (bcrypt)

JWT token-based login and route protection


📢 Announcements Module

Admin-only POST and DELETE

Viewable to all users

Role-based access control implemented


🧳 Lost & Found Module

Students can post lost/found items

Full CRUD functionality

Role check for deletion

(Optional) Image upload support




---

🗂 Project Structure

app/
├── main.py           # Entry point for FastAPI app
├── models.py         # SQLAlchemy database models
├── schemas.py        # Pydantic schemas
├── routes/           # API routes for each feature
├── database.py       # DB connection logic
└── utils/            # Utility functions (e.g., hashing, validation)


---

🛠 Setup Instructions

1. Clone the Repository

git clone https://github.com/maahhhiii/PROJECT.git
cd PROJECT

2. Create & Activate Virtual Environment

python -m venv venv
# Activate:
# Windows
venv\Scripts\activate
# Mac/Linux
source venv/bin/activate

3. Install Dependencies

pip install -r requirements.txt

4. Run the Project

uvicorn app.main:app --reload

Then open: http://127.0.0.1:8000/docs to explore Swagger UI.


---

🔐 Authentication Notes

Register a new user via /register

Login via /login to receive JWT token

Click Authorize in Swagger and paste:
Bearer <your_token_here> to access protected routes



---

🧪 Testing & Validation

All routes are tested via Swagger UI

Role-based restrictions added for admin functionalities

Password validator ensures strong user credentials

SQLite used for database; viewable using SQLite Viewer in VSCode



---

📦 Technologies Used

Python 3.11+

FastAPI

SQLAlchemy

Pydantic

JWT (via python-jose)

bcrypt (for hashing)



---

👨‍💻 Developer

Name: Mahi

Internship Project @ Syllogistek Systems



---

📎 Repository Link

👉 https://github.com/maahhhiii/PROJECT


---