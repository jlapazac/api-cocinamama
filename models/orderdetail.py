from sqlalchemy import Table, Column, ForeignKey
from sqlalchemy import Integer, String, Float
from sqlalchemy import MetaData

meta = MetaData()

ordersdetails = Table(
    'ordersdetails',meta,
    Column('id',Integer,primary_key=True),
    Column('order_id',Integer,ForeignKey('orders.id')),
    Column('publicationdetail_id',Integer,ForeignKey('publicationsdetails.id')),
    Column('typeorder',String(50)),
    Column('price',Float),
    Column('amount',Integer)
)