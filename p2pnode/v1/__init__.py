from fastapi import APIRouter

from node.v1.public import public
from node.v1.private import private

v1 = APIRouter()

v1.include_router(public, prefix="/public")
v1.include_router(private, prefix="/private")