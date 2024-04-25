import pytest
from selenium.common import JavascriptException
from selenium.webdriver.chrome.webdriver import WebDriver

from .pages.admin_tables_page import TablesPage
from .pages.admin_teachers_page import TeachersPage
from .pages.admin_logs_page import LogsPage
from .pages.auth_page import AuthPage
from .pages.admin_main_page import MainPage
from .utils.js_scripts import JSScripts
from .utils.routes import Routes
from .utils.constants import DataForTests


@pytest.fixture(scope='module')
def auth_driver(driver):
    # check if authentication is needed
    try:
        driver.execute_script(JSScripts.GET_LOCAL_STORAGE_ITEM, 'token')
        MainPage(driver, Routes.ADMIN_MAIN_URL)
    except JavascriptException:
        auth_page = AuthPage(driver, Routes.AUTH_URL)
        auth_page.authorize(DataForTests.CORRECT_PASSWORD)
    yield driver
    driver.quit()


@pytest.mark.order(2)
@pytest.mark.selenium_tests
class TestAdminViews:
    def test_should_see_admin_page_after_auth(self, auth_driver: WebDriver):
        main_page = MainPage(auth_driver, Routes.ADMIN_MAIN_URL)
        main_page.check_page(Routes.ADMIN_MAIN_URL)

    @pytest.mark.parametrize('nav_page', ['Tables', 'Teachers', 'Logs'])
    def test_should_see_page_after_nav_click(self, auth_driver: WebDriver, nav_page):
        admin_main_page = MainPage(auth_driver, Routes.ADMIN_MAIN_URL)
        if nav_page == 'Tables':
            admin_main_page.switch_to_tables_page()
            expected_page_cls = TablesPage
            url = Routes.ADMIN_TABLES_URL
        elif nav_page == 'Teachers':
            admin_main_page.switch_to_teachers_page()
            expected_page_cls = TeachersPage
            url = Routes.ADMIN_TEACHERS_URL
        elif nav_page == 'Logs':
            admin_main_page.switch_to_logs_page()
            expected_page_cls = LogsPage
            url = Routes.ADMIN_LOGS_URL
        else:
            assert False, "Something wrong with parameters"
        new_page = expected_page_cls(admin_main_page.get_driver())
        new_page.check_page(url)
