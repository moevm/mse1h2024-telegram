from selenium.common import NoSuchElementException
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


class BasePage:
    _driver = None

    # if link remains None, then no transition needed
    def __init__(self, driver: WebDriver, link=None):
        self._driver = driver
        if link:
            self._driver.get(link)

    def find_by_locator(self, locator):
        try:
            element = self._driver.find_element(locator[0], locator[1])
        except NoSuchElementException:
            assert False, f'Element not found: {self._driver.current_url=}, {locator=}'
        return element

    def get_driver(self):
        return self._driver

    def check_page(self, url):
        self.check_url_equals(url)

    def wait_until(self, until_action):
        WebDriverWait(self._driver, 10).until(
            until_action
        )

    def wait_until_url_change(self, action=None):
        prev_url = self._driver.current_url
        if action:
            action()
        self.wait_until(expected_conditions.url_changes(prev_url))

    def check_url_starts_with(self, expected):
        url = self._driver.current_url
        assert url.startswith(expected), f'{url=}, {expected=}'

    def check_url_equals(self, expected):
        url = self._driver.current_url
        assert url == expected, f'{url=}, {expected=}'
