import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

link = "http://localhost:8080/"


@pytest.fixture
def password_testcases():
    return [
        ["4321", "Неверный пароль"]
    ]


class TestAuth():

    def setup_method(self):
        self.browser = webdriver.Chrome()

    def teardown_method(self):
        self.browser.quit()

    def test_should_see_login_page(self):
        self.browser.get(link)
        self.browser.find_element(By.ID, "sign-in-button")

    def test_login_dialog(self):
        self.browser.get(link)
        login_button = self.browser.find_element(By.ID, "sign-in-button")

        assert login_button.is_enabled(), "Кнопка входа не активна"

        login_button.click()
        WebDriverWait(self.browser, 5).until(EC.presence_of_element_located(
            (By.ID, "sign-in-dialog")
        ))

    def test_correct_password(self):
        self.browser.get(link)
        login_button = self.browser.find_element(By.ID, "sign-in-button")

        assert login_button.is_enabled(), "Кнопка входа не активна"

        login_button.click()
        WebDriverWait(self.browser, 5).until(EC.presence_of_element_located(
            (By.ID, "sign-in-dialog")
        ))
        password_input = self.browser.find_element(By.ID, "password-field")
        password_input.send_keys("1234")

        confirm = self.browser.find_element(By.ID, "confirm-button")
        confirm.click()
        WebDriverWait(self.browser, 10).until(
            EC.url_changes(self.browser.current_url)
        )

        assert self.browser.current_url == (link+"admin")

    def test_incorrect_passwords(self, password_testcases):
        self.browser.get(link)
        login_button = self.browser.find_element(By.ID, "sign-in-button")

        assert login_button.is_enabled(), "Кнопка входа не активна"

        login_button.click()
        WebDriverWait(self.browser, 5).until(EC.presence_of_element_located(
            (By.ID, "sign-in-dialog")
        ))
        password_input = self.browser.find_element(By.ID, "password-field")
        for testcase in password_testcases:
            password_input.clear()
            password_input.send_keys(testcase[0])

            confirm = self.browser.find_element(By.ID, "confirm-button")
            confirm.click()

            WebDriverWait(self.browser, 5).until(
                EC.presence_of_element_located(
                    (By.ID, "password-field-messages")
                )
            )
            message = self.browser.find_element(
                By.ID,
                "password-field-messages"
            )
            assert message.text == testcase[1]
