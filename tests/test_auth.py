import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from base_selenium import BaseSelenium

link = "http://localhost:8080/"


@pytest.fixture
def password_testcases():
    return [
        ["4321", "Неверный пароль"]
    ]


class TestAuth(BaseSelenium):

    def test_should_see_login_page(self):
        self.driver.get(link)
        self.driver.find_element(By.ID, "sign-in-button")

    def test_login_dialog(self):
        self.driver.get(link)
        login_button = self.driver.find_element(By.ID, "sign-in-button")

        assert login_button.is_enabled(), "Кнопка входа не активна"

        login_button.click()
        WebDriverWait(self.driver, 5).until(EC.presence_of_element_located(
            (By.ID, "sign-in-dialog")
        ))

    def test_correct_password(self):
        self.driver.get(link)
        login_button = self.driver.find_element(By.ID, "sign-in-button")

        assert login_button.is_enabled(), "Кнопка входа не активна"

        login_button.click()
        WebDriverWait(self.driver, 5).until(EC.presence_of_element_located(
            (By.ID, "sign-in-dialog")
        ))
        password_input = self.driver.find_element(By.ID, "password-field")
        password_input.send_keys("1234")

        confirm = self.driver.find_element(By.ID, "confirm-button")
        confirm.click()
        WebDriverWait(self.driver, 10).until(
            EC.url_changes(self.driver.current_url)
        )

        assert self.driver.current_url == (link+"admin")

    def test_incorrect_passwords(self, password_testcases):
        self.driver.get(link)
        login_button = self.driver.find_element(By.ID, "sign-in-button")

        assert login_button.is_enabled(), "Кнопка входа не активна"

        login_button.click()
        WebDriverWait(self.driver, 5).until(EC.presence_of_element_located(
            (By.ID, "sign-in-dialog")
        ))
        password_input = self.driver.find_element(By.ID, "password-field")
        for testcase in password_testcases:
            password_input.clear()
            password_input.send_keys(testcase[0])

            confirm = self.driver.find_element(By.ID, "confirm-button")
            confirm.click()

            WebDriverWait(self.driver, 5).until(
                EC.presence_of_element_located(
                    (By.ID, "password-field-messages")
                )
            )
            message = self.driver.find_element(
                By.ID,
                "password-field-messages"
            )
            assert message.text == testcase[1]
