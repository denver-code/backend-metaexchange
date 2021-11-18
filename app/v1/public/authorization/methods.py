from fastapi import (
    HTTPException,
    Header
)
from app.v1.api.database_user_api import get_user
import os
import jwt
import hashlib


async def login_required(Authorization=Header("Authorization")):
    try:
        _jwt = jwt.decode(Authorization, os.getenv('SECRET_JWT', "YOURTOKENHERE"), algorithm="HS256")
        user_object = await get_user(_jwt["email"])
        if _jwt["session"] not in user_object["sessions"]:
            raise HTTPException(status_code=401, detail="Unauthorized")
    except:
        raise HTTPException(status_code=401, detail="Unauthorized")


async def get_password_hash(password):
    return hashlib.sha256(password.encode('utf-8')).hexdigest()
