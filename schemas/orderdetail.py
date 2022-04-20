from pydantic import BaseModel

class OrderDetail(BaseModel):
    order_id: int
    publicationdetail_id: int
    typeorder: str
    price: float
    amount: int