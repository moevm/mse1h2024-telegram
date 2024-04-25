import pytest
from selenium.webdriver.chrome.webdriver import WebDriver

from .pages.auth_page import AuthPage
from .pages.admin_main_page import AdminMainPage
from .utils.routes import Routes
from .utils.constants import DataForTests


@pytest.fixture(scope='module')
def auth_driver(driver):
    auth_page = AuthPage(driver, Routes.AUTH_URL)
    auth_page.authorize(DataForTests.CORRECT_PASSWORD)
    yield driver


@pytest.mark.order(2)
class TestAdmin:

    def test_should_see_admin_page_after_auth(self, auth_driver: WebDriver):
        admin_main_page = AdminMainPage(auth_driver, Routes.ADMIN_MAIN_URL)
        admin_main_page.check_page(Routes.ADMIN_MAIN_URL)
