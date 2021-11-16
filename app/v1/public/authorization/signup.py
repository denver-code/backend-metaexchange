from fastapi import (
    APIRouter,
)
from pydantic import BaseModel

signup = APIRouter(prefix="/signup")


class User(BaseModel):
    email: str
    password: str
    wallets: list
    history: list


@signup.post("/")
async def signup_event(user: User):
    return user
