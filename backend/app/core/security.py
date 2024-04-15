from typing import Any
from datetime import datetime, timedelta
import jwt

from app.config.settings import settings

ALGORITHM = "HS256"


def create_token(subject: str | Any, exp_delta: timedelta) -> str:
    expire = datetime.now() + exp_delta
    to_encode = {"exp": expire, "sub": str(subject)}
    return jwt.encode(
        payload=to_encode,
        key=settings.SECRET_KEY,
        algorithm=ALGORITHM
    )


def verify_password(req_password: str) -> bool:
    return req_password == settings.ADMIN_PASSWORD
