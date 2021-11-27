from fastapi import APIRouter

from p2pnode.v1.public import public
from p2pnode.v1.private import private

v1 = APIRouter()

v1.include_router(public, prefix="/public")
v1.include_router(private, prefix="/private")