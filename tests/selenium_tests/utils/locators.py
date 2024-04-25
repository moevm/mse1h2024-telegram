from selenium.webdriver.common.by import By


class AuthPageLocators:
    SIGN_IN_BUTTON = (By.XPATH, '//*[@data-testid="sign-in-button"]')
    SIGN_IN_DIALOG = (By.XPATH, '//*[@data-testid="sign-in-dialog"]')
    PASSWORD_FIELD = (By.XPATH, '//*[@data-testid="password-field"]//input')
    CONFIRM_BUTTON = (By.XPATH, '//*[@data-testid="confirm-button"]')
    PASSWORD_FEEDBACK = (By.XPATH, '//*[@data-testid="password-field"]//*[@class="v-input__details"]')
