from selenium.webdriver.common.by import By


class AuthPageLocators:
    SIGN_IN_BUTTON = (By.XPATH, '//*[@data-testid="sign-in-button"]')
    SIGN_IN_DIALOG = (By.XPATH, '//*[@data-testid="sign-in-dialog"]')
    PASSWORD_FIELD = (By.XPATH, '//*[@data-testid="password-field"]//input')
    CONFIRM_BUTTON = (By.XPATH, '//*[@data-testid="confirm-button"]')
    PASSWORD_FEEDBACK = (By.XPATH, '//*[@data-testid="password-field"]//*[@class="v-input__details"]')


class AdminPageLocators:
    NAV_ADMIN_TABLES = (By.XPATH, '//*[@data-testid="nav-admin-tables"]')
    NAV_ADMIN_TEACHERS = (By.XPATH, '//*[@data-testid="nav-admin-teachers"]')
    NAV_ADMIN_LOGS = (By.XPATH, '//*[@data-testid="nav-admin-logs"]')
