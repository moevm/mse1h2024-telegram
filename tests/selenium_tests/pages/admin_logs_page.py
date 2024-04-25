from .admin_main_page import MainPage

from ..utils.locators import LogsPageLocators


class LogsPage(MainPage):
    def check_page(self, url):
        super().check_page(url)
        self.find_by_locator(LogsPageLocators.LOGS_TABLE)
        self.find_by_locator(LogsPageLocators.LOGS_FILTER)
        self.find_by_locator(LogsPageLocators.SEARCH_LOGS_INPUT)
