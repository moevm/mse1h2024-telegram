from .constants import DataForTests


class Routes:
    FRONTEND_URL = DataForTests.FRONTEND_URL
    AUTH_URL = FRONTEND_URL
    ADMIN_MAIN_URL = f'{FRONTEND_URL}/admin'
    ADMIN_TABLES_URL = f'{ADMIN_MAIN_URL}/tables'
    ADMIN_TEACHERS_URL = f'{ADMIN_MAIN_URL}/teachers'
    ADMIN_LOGS_URL = f'{ADMIN_MAIN_URL}/logs'
