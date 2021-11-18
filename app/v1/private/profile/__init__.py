from fastapi import (
    APIRouter,
)
from app.v1.private.profile.profile import profile as profiler

profile = APIRouter(prefix="/profile")

profile.include_router(profiler)
