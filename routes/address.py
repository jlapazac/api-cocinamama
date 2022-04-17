from fastapi import APIRouter
from config.db import conn
from models.index import addresses
from schemas.index import Address

address = APIRouter()

@address.get('/')
async def read_data():
    return conn.execute(addresses.select()).fetchall()

@address.get('/{id}')
async def read_data(id: int):
    return conn.execute(addresses.select().where(addresses.c.id == id)).fetchall()

@address.post('/')
async def write_data(address: Address):
    conn.execute(addresses.insert().values(
        city = address.city,
        province = address.province,
        district = address.district,
        address = address.address,
        latitude = address.latitude,
        longitude = address.longitude,
        user_id = address.user_id
    ))
    return conn.execute(addresses.select()).fetchall()

@address.put('/{id}')
async def update_data(id: int, address: Address):
    conn.execute(addresses.update().values(
        city = address.city,
        province = address.province,
        district = address.district,
        address = address.address,
        latitude = address.latitude,
        longitude = address.longitude,
        user_id = address.user_id
    ).where(addresses.c.id == id))
    return conn.execute(addresses.select()).fetchall()

@address.delete('/{id}')
async def delete_data(id: int):
    conn.execute(addresses.delete().where(addresses.c.id == id))
    return conn.execute(addresses.select()).fetchall()