from fastapi import APIRouter
from config.db import conn
from models.index import orders
from schemas.index import Order, OrderComment, OrderStar, OrderUpdate, OrderState

order = APIRouter()

@order.get('/')
async def read_data():
    return conn.execute(orders.select()).fetchall()

@order.post('/')
async def write_data(order: Order):
    conn.execute(orders.insert().values(
        user_id = order.user_id,
        registerdate = order.registerdate,
        totalamount = order.totalamount,
        address_id = order.address_id,
        payment = order.payment,
        state = order.state,
        descriptionstate = order.descriptionstate,
        photo = order.photo
    ))
    return conn.execute(orders.select()).fetchall()

@order.put('/{id}')
async def update_data(id: int, order: OrderUpdate):
    conn.execute(orders.update().values(
        user_id = order.user_id,
        totalamount = order.totalamount,
        address_id = order.address_id,
        payment = order.payment,
        photo = order.photo
    ).where(orders.c.id == id))
    return conn.execute(orders.select()).fetchall()

@order.put('/comment/{id}')
async def update_data(id: int, order: OrderComment):
    conn.execute(orders.update().values(
        comment = order.comment,
    ).where(orders.c.id == id))
    return conn.execute(orders.select()).fetchall()

@order.put('/star/{id}')
async def update_data(id: int, order: OrderStar):
    conn.execute(orders.update().values(
        star = order.star
    ).where(orders.c.id == id))
    return conn.execute(orders.select()).fetchall()

@order.put('/state/{id}')
async def update_data(id: int, order: OrderState):
    conn.execute(orders.update().values(
        state = order.state,
        descriptionstate = order.descriptionstate
    ).where(orders.c.id == id))
    return conn.execute(orders.select()).fetchall()