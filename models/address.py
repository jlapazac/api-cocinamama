from sqlalchemy import Table, Column, ForeignKey
from sqlalchemy.sql.sqltypes import Integer,String,Float
from sqlalchemy import MetaData

meta = MetaData()

addresses = Table(
    'addresses',meta,
    Column('id',Integer,primary_key=True),
    Column('city',String(200)),
    Column('province',String(200)),
    Column('district',String(200)),
    Column('address',String(200)),
    Column('latitude',Float),
    Column('longitude',Float),
    Column('user_id',Integer,ForeignKey('users.id'))
)