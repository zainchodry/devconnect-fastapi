# 🚀 DevConnect – FastAPI Job & Project Marketplace API

DevConnect is a professional-level backend system built with **FastAPI** where:
- Clients can post freelance projects or jobs
- Developers can register, browse, and apply for projects
- Authentication is powered by JWT tokens
- Built using SQLAlchemy ORM and modern Python practices

---

## 🔧 Features

- ✅ User registration & login (JWT-based)
- ✅ Role-based access control (`client` and `developer`)
- ✅ Clients can post jobs/projects
- ✅ Developers can send applications/proposals
- ✅ Protected API routes
- ✅ Secure password hashing with bcrypt
- ✅ Modular, professional project structure
- ✅ SQLite by default (can switch to PostgreSQL)

---

## 📁 Project Structure

devconnect/
├── app/
│ ├── init.py
│ ├── main.py
│ ├── auth.py
│ ├── crud.py
│ ├── deps.py
│ ├── database.py
│ ├── models.py
│ ├── schemas.py
│ └── routers/
│ ├── users.py
│ ├── projects.py
│ └── applications.py
├── .env
├── .gitignore
├── requirements.txt
└── README.md



---

## 🛠️ Technologies Used

- [FastAPI](https://fastapi.tiangolo.com/)
- [SQLAlchemy](https://www.sqlalchemy.org/)
- [Pydantic](https://pydantic-docs.helpmanual.io/)
- [python-jose](https://github.com/mpdavis/python-jose)
- [passlib](https://passlib.readthedocs.io/)
- [Uvicorn](https://www.uvicorn.org/)
- [dotenv](https://pypi.org/project/python-dotenv/)

---

## ⚙️ Setup Instructions

### 1. Clone the Repo

```bash
git clone https://github.com/yourusername/devconnect-fastapi.git
cd devconnect-fastapi


#2. Create & Activate Virtual Environment
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate



#3. Install Dependencies
pip install -r requirements.txt



5. Run the App

uvicorn app.main:app --reload