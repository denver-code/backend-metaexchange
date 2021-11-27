from fastapi import (
    APIRouter,
)
from app.v1.public.authorization import auth
from app.v1.schemas.blockchain import Blockchain

public = APIRouter(prefix="/public")

public.include_router(auth)

