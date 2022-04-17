from sqlalchemy import Table, Column
from sqlalchemy.sql.sqltypes import Integer, String, DateTime
from sqlalchemy import MetaData

meta = MetaData()

publications = Table(
    'publications',meta,
    Column('id',Integer,primary_key=True),
    Column('title',String(255)),
    Column('description',String(255)),
    Column('datepublish',DateTime),
    Column('photo',String(255))
)