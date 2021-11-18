from pydantic import (
    BaseModel,
    validator
)
from typing import Optional
import re


class User(BaseModel):
    email: str
    password: str
    wallets: Optional[list] = []
    history: Optional[list] = []
    sessions: Optional[list] = []

    @validator("email")
    def email_regex(cls, v):
        regex = r"\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b"
        if not re.fullmatch(regex, v):
            raise ValueError("Invalid email")
        return v

    @validator("password")
    def password_hash_checker(cls, v):
        regex = r"^[a-fA-F0-9]{64}$"
        if not re.fullmatch(regex, v):
            raise ValueError("Need hashed password")
        return v
