from typing import Annotated
from fastapi import Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer
import jwt

from app.config.settings import settings
from app.core import security
from app.schemas.auth import TokenPayload

oauth2 = OAuth2PasswordBearer(
    tokenUrl=f"{settings.API_STR}/auth/login",
)

TokenDep = Annotated[str, Depends(oauth2)]


def get_admin(token: TokenDep) -> TokenPayload:
    try:
        payload = jwt.decode(
            token, settings.SECRET_KEY, [security.ALGORITHM]
        )
        token_payload = TokenPayload(**payload)
    except jwt.DecodeError:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="Could not validate credentials"
        )
    return token_payload


Admin = Annotated[TokenPayload, Depends(get_admin)]
