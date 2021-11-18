from fastapi import (
    APIRouter,
)
from app.v1.public.authorization.signup import signup
from app.v1.public.authorization.signin import signin
from app.v1.public.authorization.logout import logout

auth = APIRouter(prefix="/authorization")

auth.include_router(signup)
auth.include_router(signin)
auth.include_router(logout)