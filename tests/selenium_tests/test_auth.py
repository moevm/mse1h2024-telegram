import pytest
from selenium.webdriver.chrome.webdriver import WebDriver

from .pages.auth_page import AuthPage
from .pages.admin_page_main import AdminMainPage
from .utils.routes import Routes
from .utils.constants import DataForTests


class TestAuth:

    def test_should_see_login_page(self, driver: WebDriver):
        auth_page = AuthPage(driver, Routes.AUTH_URL)
        auth_page.check_page(Routes.AUTH_URL)

    def test_correct_password(self, driver: WebDriver):
        auth_page = AuthPage(driver, Routes.AUTH_URL)
        auth_page.authorize(DataForTests.CORRECT_PASSWORD)
        admin_page = AdminMainPage(auth_page.get_browser())
        admin_page.check_page(Routes.ADMIN_MAIN_URL)

    @pytest.mark.parametrize("incorrect_password", ['4321', 'hello_world'])
    def test_incorrect_passwords(self, driver: WebDriver, incorrect_password):
        auth_page = AuthPage(driver, Routes.AUTH_URL)
        auth_page.authorize(incorrect_password)
        auth_page.check_page(Routes.AUTH_URL)
