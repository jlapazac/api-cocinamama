from fastapi import APIRouter
from config.db import conn
from models.index import publicationsdetails
from schemas.index import PublicationDetail

publicationdetail = APIRouter()

@publicationdetail.get('/publication/{id}')
async def read_data(id: int):
    return conn.execute(publicationsdetails.select().where(publicationsdetails.c.publication_id == id)).fetchall()

@publicationdetail.post('/')
async def write_data(publicationdetail: PublicationDetail):
    conn.execute(publicationsdetails.insert().values(
        title = publicationdetail.title,
        description = publicationdetail.description,
        price = publicationdetail.price,
        photo = publicationdetail.photo,
        publication_id = publicationdetail.publication_id
    ))
    return conn.execute(publicationsdetails.select()).fetchall()