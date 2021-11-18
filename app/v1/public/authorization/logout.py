from fastapi import (
    APIRouter,
    Depends,
    HTTPException,
    Header
)
from fastapi_limiter.depends import RateLimiter

import os
import jwt

from app.v1.public.authorization.methods import login_required

from app.v1.api.database_user_api import (
    get_user,
    update_user
)

logout = APIRouter(prefix="/logout")


@logout.get("/", dependencies=[Depends(login_required), Depends(RateLimiter(times=1, seconds=5))])
async def logout_event(Authorization=Header("Authorization")):
    _jwt = jwt.decode(Authorization, os.getenv('SECRET_JWT', "YOURTOKENHERE"), algorithm="HS256")
    user_object = await get_user(_jwt["email"])
    if _jwt["session"] in user_object["sessions"]:
        del user_object["sessions"][user_object["sessions"].index(_jwt["session"])]
        await update_user(_jwt["email"], user_object)
        return {"ok"}
    else:
        raise HTTPException(status_code=401, detail="Unauthorized")