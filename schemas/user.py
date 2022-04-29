from pydantic import BaseModel

class User(BaseModel):
    name: str
    email: str
    password: str
    phone: str
    photo: str

class Login(BaseModel):
    email: str
    password: str