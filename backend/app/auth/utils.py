from fastapi import Response, Request, HTTPException, status
from uuid import uuid4
from ..schemas.auth import TelegramAuth


# TODO: change storage for session
_session = {}
_day_in_seconds = 86400


def establish_cookie_session(response: Response, data: TelegramAuth):
    """
    Establish cookie session
    Function save telegram data (id, username, auth_date) in session storage.
    And sets the corresponding session cookie to response
    """
    uuid = uuid4()
    _session[uuid] = {
        "id": data.id,
        "username": data.username,
        "auth_date": data.auth_date
    }
    response.set_cookie("sid", uuid, _day_in_seconds, secure=True, httponly=True)


def end_cookie_session(session_uuid: str, response: Response):
    """
    Function delete user data from session storage.
    And delete corresponding session cookie
    """
    _session.pop(session_uuid)
    response.delete_cookie("sid", secure=True, httponly=True)


def get_auth_user(request: Request) -> dict:
    """
    Get user data from session storage
    """
    session_uuid = request.cookies.get("sid")
    if session_uuid is None:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Session id is not provided"
        )
    user = _session.get(session_uuid, None)
    if user is None:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="Session expired"
        )
    return user