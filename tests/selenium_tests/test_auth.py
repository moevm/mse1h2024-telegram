import pytest
from selenium.webdriver.chrome.webdriver import WebDriver

from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec

link = "http://localhost:8080/"


class TestAuth:

    def test_should_see_login_page(self, driver: WebDriver):
        driver.get(link)
        driver.find_element(By.ID, "sign-in-button")

    def test_login_dialog(self, driver: WebDriver):
        driver.get(link)
        login_button = driver.find_element(By.ID, "sign-in-button")

        assert login_button.is_enabled(), "Кнопка входа не активна"

        login_button.click()
        WebDriverWait(driver, 5).until(ec.presence_of_element_located(
            (By.ID, "sign-in-dialog")
        ))

    def test_correct_password(self, driver: WebDriver):
        driver.get(link)
        login_button = driver.find_element(By.ID, "sign-in-button")

        assert login_button.is_enabled(), "Кнопка входа не активна"

        login_button.click()
        WebDriverWait(driver, 5).until(ec.presence_of_element_located(
            (By.ID, "sign-in-dialog")
        ))
        password_input = driver.find_element(By.ID, "password-field")
        password_input.send_keys("1234")

        confirm = driver.find_element(By.ID, "confirm-button")
        confirm.click()
        WebDriverWait(driver, 10).until(
            ec.url_changes(driver.current_url)
        )

        assert driver.current_url == (link + "admin")

    @pytest.mark.parametrize("password,feedback", [('4321', 'Неверный пароль')])
    def test_incorrect_passwords(self, driver: WebDriver, password, feedback):
        driver.get(link)
        login_button = driver.find_element(By.ID, "sign-in-button")

        assert login_button.is_enabled(), "Кнопка входа не активна"

        login_button.click()
        WebDriverWait(driver, 5).until(ec.presence_of_element_located(
            (By.ID, "sign-in-dialog")
        ))
        password_input = driver.find_element(By.ID, "password-field")

        password_input.clear()
        password_input.send_keys(password)

        confirm = driver.find_element(By.ID, "confirm-button")
        confirm.click()

        WebDriverWait(driver, 5).until(
            ec.presence_of_element_located(
                (By.ID, "password-field-messages")
            )
        )
        message = driver.find_element(
            By.ID,
            "password-field-messages"
        )
        assert message.text == feedback
