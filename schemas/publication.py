from datetime import datetime
from pydantic import BaseModel

class Publication(BaseModel):
    title: str
    description: str
    datepublish: datetime
    photo: str