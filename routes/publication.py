from fastapi import APIRouter
from config.db import conn
from models.index import publications
from schemas.index import Publication

publication = APIRouter()

@publication.get('/')
async def read_data():
    return conn.execute(publications.select()).fetchall()

@publication.post('/')
async def write_data(publication: Publication):
    conn.execute(publications.insert().values(
        title = publication.title,
        description = publication.description,
        datepublish = publication.datepublish,
        photo = publication.photo
    ))
    return conn.execute(publications.select()).fetchall()