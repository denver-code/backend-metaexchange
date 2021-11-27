from fastapi import (
    APIRouter,
)
import app.v1.public as public
import app.v1.private as private
import app.v1.blockchain as blockchain

api = APIRouter(prefix="/v1")

api.include_router(public.public)
api.include_router(private.private)
api.include_router(blockchain.blockchain)