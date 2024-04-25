import pytest
from selenium.common import JavascriptException
from selenium.webdriver.chrome.webdriver import WebDriver

from .pages.admin_tables_page import AdminTablesPage
from .pages.auth_page import AuthPage
from .pages.admin_main_page import AdminMainPage
from .utils.js_scripts import JSScripts
from .utils.routes import Routes
from .utils.constants import DataForTests


@pytest.fixture(scope='module')
def auth_driver(driver):
    # check if authentication is needed
    try:
        driver.execute_script(JSScripts.GET_LOCAL_STORAGE_ITEM, 'token')
        AdminMainPage(driver, Routes.ADMIN_MAIN_URL)
    except JavascriptException:
        auth_page = AuthPage(driver, Routes.AUTH_URL)
        auth_page.authorize(DataForTests.CORRECT_PASSWORD)
    yield driver


@pytest.mark.order(2)
@pytest.mark.selenium_tests
class TestAdminViews:
    def test_should_see_admin_page_after_auth(self, auth_driver: WebDriver):
        admin_main_page = AdminMainPage(auth_driver, Routes.ADMIN_MAIN_URL)
        admin_main_page.check_page(Routes.ADMIN_MAIN_URL)

    def test_should_see_tables_page_after_tables_nav_click(self, auth_driver: WebDriver):
        admin_main_page = AdminMainPage(auth_driver, Routes.ADMIN_MAIN_URL)
        admin_main_page.switch_to_tables_page()
        tables_page = AdminTablesPage(admin_main_page.get_driver())
