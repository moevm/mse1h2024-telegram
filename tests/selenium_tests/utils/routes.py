from .constants import DataForTests


class Routes:
    AUTH_URL = f'{DataForTests.FRONTEND_URL}/'
    ADMIN_MAIN_URL = f'{DataForTests.FRONTEND_URL}/admin'
    ADMIN_TABLES_URL = f'{ADMIN_MAIN_URL}/tables'
    ADMIN_TEACHERS_URL = f'{ADMIN_MAIN_URL}/teachers'
    ADMIN_LOGS_URL = f'{ADMIN_MAIN_URL}/logs'
