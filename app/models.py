from sqlalchemy import Column, String, ForeignKey, Integer, Float,Enum,Text
from sqlalchemy.orm import relationship
from app.database import Base,engine
import enum


def create_tables():
    Base.metadata.create_all(engine)

class Role(str, enum.Enum):
    client = "client"
    developer = "developer"


class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True, index=True)
    email = Column(String, unique=True, index=True)
    hashed_password = Column(String)
    role = Column(Enum(Role))


    projects = relationship("Project", back_populates="owner")
    applications = relationship("Application", back_populates="developer")


class Project(Base):
    __tablename__ = "projects"
    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, index = True)
    description = Column(Text)
    owner_id = Column(Integer, ForeignKey("users.id"))

    owner = relationship("User", back_populates="projects")
    applications = relationship("Application", back_populates="project")


class Application(Base):
    __tablename__ = "applications"
    id = Column(Integer, primary_key=True, index=True)
    project_id = Column(Integer, ForeignKey("projects.id"))
    developer_id = Column(Integer, ForeignKey("users.id"))
    proposal = Column(Text)

    project = relationship("Project", back_populates="applications")
    developer = relationship("User", back_populates="applications")

