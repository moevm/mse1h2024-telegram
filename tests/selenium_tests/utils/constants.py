import os


class DataForTests:
    FRONTEND_URL = 'http://localhost:8080/'
    INCORRECT_PASSWORD_FEEDBACK = 'Неверный пароль'
    CORRECT_PASSWORD = os.getenv('ADMIN_PASSWORD')
