from fastapi import APIRouter
from config.db import conn
from models.orderdetail import ordersdetails
from schemas.orderdetail import OrderDetail

orderdetail = APIRouter()

@orderdetail.post('/')
async def write_data(orderdetail: OrderDetail):
    conn.execute(ordersdetails.insert().values(
        order_id = orderdetail.order_id,
        publicationdetail_id = orderdetail.publicationdetail_id,
        typeorder = orderdetail.typeorder,
        price = orderdetail.price,
        amount = orderdetail.amount
    ))
    return conn.execute(ordersdetails.select()).fetchall()

@orderdetail.get('/order/{id}')
async def read_data(id: int):
    return conn.execute(ordersdetails.select().where(ordersdetails.c.order_id == id)).fetchall()