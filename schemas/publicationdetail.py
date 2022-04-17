from pydantic import BaseModel

class PublicationDetail(BaseModel):
    title: str
    description: str
    price: float
    photo: str
    publication_id: int