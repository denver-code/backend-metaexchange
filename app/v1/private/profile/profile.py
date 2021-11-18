from fastapi import (
    APIRouter,
    Depends
)
from fastapi_limiter.depends import RateLimiter
from app.v1.public.authorization.methods import login_required

profile = APIRouter(prefix="/profile")


@profile.post("/", dependencies=[Depends(login_required), Depends(RateLimiter(times=3, seconds=5))])
async def profile_event():
    pass