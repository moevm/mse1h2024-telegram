from .base_page import BasePage
from ..utils.locators import AuthPageLocators
from ..utils.constants import DataForTests


class AuthPage(BasePage):
    def _open_sign_in_pop_up(self):
        login_button = self.find_by_locator(AuthPageLocators.SIGN_IN_BUTTON)
        assert login_button.is_enabled(), "Кнопка входа не активна"
        login_button.click()
        assert self.find_by_locator(AuthPageLocators.SIGN_IN_DIALOG)

    def authorize(self, password, fail=False):
        self._open_sign_in_pop_up()

        password_field = self.find_by_locator(AuthPageLocators.PASSWORD_FIELD)
        password_field.send_keys(password)

        confirm_button = self.find_by_locator(AuthPageLocators.CONFIRM_BUTTON)

        if fail:
            confirm_button.click()
            feedback = self.find_by_locator(AuthPageLocators.PASSWORD_FEEDBACK)
            assert feedback.text == DataForTests.INCORRECT_PASSWORD_FEEDBACK
        else:
            self.wait_until_url_change(confirm_button.click)

    def check_page(self, url):
        super().check_page(url)
        assert self.find_by_locator(AuthPageLocators.SIGN_IN_BUTTON)
