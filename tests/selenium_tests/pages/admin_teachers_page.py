from .admin_main_page import MainPage

from ..utils.locators import TeachersPageLocators


class TeachersPage(MainPage):
    def check_page(self, url):
        super().check_page(url)
        self.find_by_locator(TeachersPageLocators.ADD_TEACHER_BUTTON)
        self.find_by_locator(TeachersPageLocators.TEACHERS_TABLE)
        self.find_by_locator(TeachersPageLocators.SEARCH_TEACHERS_INPUT)
