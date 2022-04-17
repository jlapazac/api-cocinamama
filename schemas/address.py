from pydantic import BaseModel

class Address(BaseModel):
    city: str
    province: str
    district: str
    address: str
    latitude: float
    longitude: float
    user_id: int