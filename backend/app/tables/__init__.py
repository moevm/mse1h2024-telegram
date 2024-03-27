import os
import json
from gspread_asyncio import (
    AsyncioGspreadClientManager,
    AsyncioGspreadClient
)
from google.oauth2.service_account import Credentials
from ..config.settings import settings


def get_creds():
    creds_json = json.loads(settings.GDRIVE_API_CREDENTIALS)
    creds = Credentials.from_service_account_info(
        creds_json
    )
    scoped = creds.with_scopes([
        "https://spreadsheets.google.com/feeds",
        "https://www.googleapis.com/auth/spreadsheets",
        "https://www.googleapis.com/auth/drive",
    ])
    return scoped


_agcm = AsyncioGspreadClientManager(get_creds)


async def get_client() -> AsyncioGspreadClient:
    return await _agcm.authorize()
