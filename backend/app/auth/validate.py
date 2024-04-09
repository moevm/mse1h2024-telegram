import hashlib
import hmac
import time

from .exceptions import TelegramHashException, TelegramDataOutdate
from ..schemas import auth
from ..config.settings import settings

SECRET_KEY = hashlib.sha256(settings.TELEGRAM_BOT_TOKEN.encode()).digest()


def validate_telegram_authorization(data: auth.TelegramAuth) -> auth.TelegramAuth:
    """
    Checking the authorization telegram data.
    Official telegram doc: https://core.telegram.org/widgets/login
    Raise TelegramHashException if hash is not provided or is incorrect.
    Raise TelegramDataOutdate if outdated data providied
    :return: Telegram Data without hash
    """
    data_dict = data.dict()
    data_hash = data_dict.pop("hash")

    if data_hash is None:
        raise TelegramHashException(
            "No hash provided"
        )

    if not _is_correct_auth_date(data_dict["auth_date"]):
        raise TelegramDataOutdate(
            "Data is outdated"
        )

    if _generate_hash(data_dict) != data_hash:
        raise TelegramHashException(
            "Incorrect hash provided"
        )

    return auth.TelegramAuth.parse_obj(data_dict)


def _is_correct_auth_date(auth_date: str) -> bool:
    """
    Function checks if outdated data is providied
    """
    day_in_seconds = 86400
    time_now = int(time.time())
    time_auth_date = int(auth_date)
    return (time_now - time_auth_date) < day_in_seconds


def _generate_hash(data: dict) -> str:
    """
    Function generate hash from recived data fields
    """
    strings_array = []
    for key, val in data.items():
        if val is not None:
            strings_array.append(f"{key}={val}")
    strings_array.sort()
    string_cat = '\n'.join(strings_array)
    return hmac.new(
        key=SECRET_KEY,
        msg=string_cat.encode(),
        digestmod=hashlib.sha256
    ).hexdigest()
