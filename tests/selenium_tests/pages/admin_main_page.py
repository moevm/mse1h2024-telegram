from .base_page import BasePage
from ..utils.locators import MainPageLocators


class MainPage(BasePage):

    def switch_to_tables_page(self):
        self._switch_to_page_by_locator(MainPageLocators.NAV_TABLES)

    def switch_to_teachers_page(self):
        self._switch_to_page_by_locator(MainPageLocators.NAV_TEACHERS)

    def switch_to_logs_page(self):
        self._switch_to_page_by_locator(MainPageLocators.NAV_LOGS)

    def _switch_to_page_by_locator(self, locator):
        tables_link = self.find_by_locator(locator)
        self.wait_until_url_change(tables_link.click)

    def check_page(self, url):
        super().check_page(url)
        self.find_by_locator(MainPageLocators.NAV_TABLES)
        self.find_by_locator(MainPageLocators.NAV_TEACHERS)
        self.find_by_locator(MainPageLocators.NAV_LOGS)
