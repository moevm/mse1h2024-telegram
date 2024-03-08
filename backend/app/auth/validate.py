import os
import hashlib
import hmac
import time

from .exceptions import TelegramHashException, TelegramDataOutdate
from ..schemas import auth


SECRET_KEY = hashlib.sha256(os.getenv("TELEGRAM_BOT_TOKEN").encode()).digest()


def validate_telegram_authorization(data: auth.TelegramAuth) -> dict:
    """
    Checking the authorization telegram data.
    Official telegram doc: https://core.telegram.org/widgets/login
    Raise TelegramHashException if hash is not provided or is incorrect.
    :return: Telegram Data without hash
    """
    data_dict = data.model_dump()
    hash = data_dict.pop("hash")

    if hash is None:
        raise TelegramHashException(
            "No hash provided"
        )
    
    if _is_correct_auth_date(data_dict["auth_date"]) == False:
        raise TelegramDataOutdate(
            "Data is outdated"
        )
        
    if _generate_hash(data_dict) != hash:
        raise TelegramHashException(
            "Incorrect hash provided"
        )
    
    return data_dict


def _is_correct_auth_date(auth_date: str) -> bool:
    day_in_seconds = 86400
    time_now = int(time.time())
    time_auth_date = int(auth_date)
    return (time_now-time_auth_date) < day_in_seconds


def _generate_hash(data: dict) -> str:
    alphabetical_data_order = sorted(data.items(),key=lambda item: item[0])
    data_check_string = '\n'.join(
        [f"{key}={value}" for key, value in alphabetical_data_order]
    )
    return hmac.new(
        key=SECRET_KEY,
        msg=data_check_string.encode(),
        digestmod=hashlib.sha256
    ).hexdigest()
    