class Routes:
    FRONTEND_URL = 'http://localhost:8080'

    @property
    def AUTH_URL(self):
        return self.FRONTEND_URL

    @property
    def ADMIN_MAIN_URL(self):
        return f'{self.FRONTEND_URL}/admin'

    @property
    def ADMIN_TABLES_URL(self):
        return f'{self.ADMIN_MAIN_URL}/tables'

    @property
    def ADMIN_TEACHERS_URL(self):
        return f'{self.ADMIN_MAIN_URL}/teachers'

    @property
    def ADMIN_LOGS_URL(self):
        return f'{self.ADMIN_MAIN_URL}/logs'
