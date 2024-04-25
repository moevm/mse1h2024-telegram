from .admin_main_page import MainPage

from ..utils.locators import TablesPageLocators


class TablesPage(MainPage):
    def check_page(self, url):
        super().check_page(url)
        self.find_by_locator(TablesPageLocators.ADD_TABLE_BUTTON)
