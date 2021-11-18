from fastapi import (
    APIRouter,
    Depends,
    HTTPException
)
from fastapi_limiter.depends import RateLimiter
from pydantic import (
    BaseModel,
    validator
)
import re
import jwt
import os
from app.v1.api.database_user_api import (
    insert_user,
    user_exist,
    get_user,
    update_user
)
from app.v1.schemas.user import User
from uuid import uuid4


signin = APIRouter(prefix="/signin")


@signin.post("/", dependencies=[Depends(RateLimiter(times=1, seconds=5))])
async def signin_event(user: User):
    if not await user_exist(user.email):
        raise HTTPException(status_code=404, detail="User not exist")
    _user = await get_user(user.email)
    if user.password == _user["password"]:
        _user["sessions"].append(str(uuid4()))
        token = jwt.encode({
                    "email": user.email,
                    "session": _user["sessions"][-1]
                }, os.getenv('SECRET_JWT', "YOURTOKENHERE"), algorithm="HS256")
        await update_user(user.email, _user)
        return {"token": token}
    else:
        raise HTTPException(status_code=403, detail="Forbidden")

