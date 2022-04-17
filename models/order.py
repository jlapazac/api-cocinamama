from sqlalchemy import Table, Column, ForeignKey
from sqlalchemy.sql.sqltypes import Integer, String, Float, DateTime
from sqlalchemy import MetaData

meta = MetaData()

orders = Table(
    'orders',meta,
    Column('id',Integer,primary_key=True),
    Column('user_id',Integer,ForeignKey('users.id')),
    Column('registerdate',DateTime),
    Column('totalamount',Float),
    Column('address_id',Integer,ForeignKey('addresses.id')),
    Column('payment',String(255)),
    Column('state',String(255)),
    Column('descriptionstate',String(800)),
    Column('photo',String(255)),
    Column('comment',String(800)),
    Column('star',Integer)
)