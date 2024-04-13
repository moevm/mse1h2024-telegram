from fastapi import APIRouter, Depends, Response, HTTPException, status
from ..schemas.auth import TelegramAuth
from ..auth.exceptions import TelegramHashException, TelegramDataOutdate
from ..auth.validate import validate_telegram_authorization
from ..auth import utils

router = APIRouter(
    prefix="/auth",
    tags=["auth"]
)


@router.get("/login", responses={
    400: {"description": "Incorrect hash provided"},
    401: {"description": "Data is outdated"}
})
async def login_handler(response: Response, query_params: TelegramAuth = Depends()):
    """
    Endpoint for authorization through Telegram API.

    Return 400 Bad Request if hash is not provided or is incorrect.

    Return 401 Unauthorized if outdated data provided.
    """
    # TODO: Check is admin
    try:
        data = validate_telegram_authorization(query_params)
    except TelegramHashException:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST
        )
    except TelegramDataOutdate:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED
        )
    utils.establish_cookie_session(response, data)
    return {
        "message": "Cookie session successfully establish"
    }
