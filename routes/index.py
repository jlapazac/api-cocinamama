from fastapi import APIRouter
from routes import address, user, publication, publicationdetail, order, orderdetail

api_router = APIRouter()
api_router.include_router(user.user, prefix="/user", tags=["user"])
api_router.include_router(address.address, prefix="/address", tags=["address"])
api_router.include_router(publication.publication, prefix="/publication", tags=["publication"])
api_router.include_router(publicationdetail.publicationdetail, prefix="/publicationdetail", tags=["publicationdetail"])
api_router.include_router(order.order, prefix="/order", tags=["order"])
api_router.include_router(orderdetail.orderdetail, prefix="/orderdetail", tags=["orderdetail"])