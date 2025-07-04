from pydantic import BaseModel, EmailStr
from typing import List, Optional
import enum

class Role(str, enum.Enum):
    client = "client"
    developer = "developer"


class UserCreate(BaseModel):
    email: EmailStr
    password:str
    role:Role

class UserOut(BaseModel):
    id:int
    email:EmailStr
    role:Role


    class Config:
        orm_mode = True



class Token(BaseModel):
    access_token:str
    token_type:str


class TokenData(BaseModel):
    id: Optional[int] = None



class ProjectCreate(BaseModel):
    title: str
    description: str

class ProjectOut(ProjectCreate):
    id: int
    owner_id: int
    class Config:
        orm_mode = True

class ApplicationCreate(BaseModel):
    project_id: int
    proposal: str

class ApplicationOut(ApplicationCreate):
    id: int
    developer_id: int
    class Config:
        orm_mode = True
