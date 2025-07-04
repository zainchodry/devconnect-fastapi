from fastapi import FastAPI
from app.routes import users, projects, applications
from app.database import Base,engine


Base.metadata.create_all(bind=engine)

app = FastAPI(title = "DevConnect API")


app.include_router(users.router)
app.include_router(projects.router)
app.include_router(applications.router)


