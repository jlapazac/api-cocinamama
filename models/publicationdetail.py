from sqlalchemy import Table, Column, ForeignKey
from sqlalchemy.sql.sqltypes import Integer, String, Float
from sqlalchemy import MetaData

meta = MetaData()

publicationsdetails = Table(
    'publicationsdetails',meta,
    Column('id',Integer,primary_key=True),
    Column('title',String(255)),
    Column('description',String(255)),
    Column('price',Float),
    Column('photo',String(255)),
    Column('publication_id',Integer,ForeignKey('publications.id'))
)