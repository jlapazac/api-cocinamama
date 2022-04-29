from fastapi import APIRouter
from config.db import conn
from models.index import users
from schemas.index import User, Login

user = APIRouter()

@user.get('/')
async def read_data():
    return conn.execute(users.select()).fetchall()

@user.post('/login/')
async def login(user: Login):
    login = get_user(user.email, user.password)
    success = False
    if (login == []):
        success = False
    else:
        success = True
    return success

def get_user(email: str, password: str):
    return conn.execute(users.select().where(users.c.email == email, users.c.password == password)).fetchall()

@user.get('/{id}')
async def read_data(id: int):
    return conn.execute(users.select().where(users.c.id == id)).fetchall()

@user.post('/')
async def write_data(user: User):
    conn.execute(users.insert().values(
        name = user.name,
        email = user.email,
        password = user.password,
        phone = user.phone,
        photo = user.photo
    ))
    return conn.execute(users.select()).fetchall()

@user.put('/{id}')
async def update_data(id: int, user: User):
    conn.execute(users.update().values(
        name = user.name,
        email = user.email,
        password = user.password,
        phone = user.phone,
        photo = user.photo
    ).where(users.c.id == id))
    return conn.execute(users.select()).fetchall()

@user.delete('/{id}')
async def delete_data(id: int):
    conn.execute(users.delete().where(users.c.id == id))
    return conn.execute(users.select()).fetchall()