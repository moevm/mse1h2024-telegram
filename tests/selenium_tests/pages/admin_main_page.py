from .base_page import BasePage
from ..utils.locators import AdminPageLocators


class AdminMainPage(BasePage):

    def switch_to_tables_page(self):
        self._switch_to_page_by_locator(AdminPageLocators.NAV_ADMIN_TABLES)

    def switch_to_teachers_page(self):
        self._switch_to_page_by_locator(AdminPageLocators.NAV_ADMIN_TEACHERS)

    def switch_to_logs_page(self):
        self._switch_to_page_by_locator(AdminPageLocators.NAV_ADMIN_LOGS)

    def _switch_to_page_by_locator(self, locator):
        tables_link = self.find_by_locator(locator)
        self.wait_until_url_change(tables_link.click())

    def check_page(self, url):
        super().check_page(url)
        self.find_by_locator(AdminPageLocators.NAV_ADMIN_TABLES)
        self.find_by_locator(AdminPageLocators.NAV_ADMIN_TEACHERS)
        self.find_by_locator(AdminPageLocators.NAV_ADMIN_LOGS)
