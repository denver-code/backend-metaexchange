from fastapi import (
    APIRouter,
    Depends,
    HTTPException
)
from fastapi_limiter.depends import RateLimiter
import jwt
import os
from app.v1.api.database_user_api import (
    insert_user,
    user_exist
)
from uuid import uuid4
from app.v1.schemas.user import User

signup = APIRouter(prefix="/signup")


@signup.post("/", dependencies=[Depends(RateLimiter(times=1, seconds=5))])
async def signup_event(user: User):
    user = User(email=user.email,
                password=user.password,
                sessions=[str(uuid4())]).dict()
    if not await user_exist(user["email"]):
        if not await insert_user(user):
            raise HTTPException(status_code=500, detail="Internal Server Error")
        token = jwt.encode({
                    "email": user["email"],
                    "session": user["sessions"][0]
                }, os.getenv('SECRET_JWT', "YOURTOKENHERE"), algorithm="HS256")
        return {"token": token}
    raise HTTPException(status_code=403, detail="User already exist")
