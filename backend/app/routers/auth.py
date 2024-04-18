from typing import Annotated
from datetime import timedelta
from fastapi import APIRouter, HTTPException, status, Depends
from fastapi.security import OAuth2PasswordRequestForm
from app.schemas.auth import Token
from app.config.settings import settings
from app.core import security
from app.deps import Admin

router = APIRouter(
    prefix="/auth",
    tags=["auth"]
)


@router.post("/login", responses={
    400: {"description": "Incorrect password provided"}
})
async def login_handler(form_data: Annotated[
    OAuth2PasswordRequestForm,
    Depends()]
) -> Token:
    """
    Endpoint for authorization, return access token

    Return 400 Bad Request if password is incorrect
    """
    if not security.verify_password(form_data.password):
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Incorrect password"
        )
    return Token(
        access_token=security.create_token(
            subject="OKAY",
            exp_delta=timedelta(minutes=settings.TOKEN_EXPIRE_MINUTES)
        )
    )


@router.get("/test-token")
async def test_token(admin: Admin):
    """
    Test access token
    """
    return admin
