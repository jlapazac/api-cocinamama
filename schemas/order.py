from datetime import datetime
from pydantic import BaseModel

class Order(BaseModel):
    user_id: int
    registerdate: datetime
    totalamount: float
    address_id: int
    payment: str
    state: str
    descriptionstate: str
    photo: str
    
class OrderComment(BaseModel):
    comment: str

class OrderStar(BaseModel):
    star: int
    
class OrderUpdate(BaseModel):
    user_id: int
    totalamount: float
    address_id: int
    payment: str
    photo: str

class OrderState(BaseModel):
    state: str
    descriptionstate: str