from selenium.webdriver.common.by import By


class AuthPageLocators:
    SIGN_IN_BUTTON = (By.XPATH, '//*[@data-testid="sign-in-button"]')
    SIGN_IN_DIALOG = (By.XPATH, '//*[@data-testid="sign-in-dialog"]')
    PASSWORD_FIELD = (By.XPATH, '//*[@data-testid="password-field"]//input')
    CONFIRM_BUTTON = (By.XPATH, '//*[@data-testid="confirm-button"]')
    PASSWORD_FEEDBACK = (By.XPATH, '//*[@data-testid="password-field"]//*[@class="v-input__details"]')


class MainPageLocators:
    NAV_TABLES = (By.XPATH, '//*[@data-testid="nav-admin-tables"]')
    NAV_TEACHERS = (By.XPATH, '//*[@data-testid="nav-admin-teachers"]')
    NAV_LOGS = (By.XPATH, '//*[@data-testid="nav-admin-logs"]')


class TablesPageLocators(MainPageLocators):
    ADD_TABLE_BUTTON = (By.XPATH, '//*[@data-testid="add-table-button"]')
    ADD_RULE_BUTTON = (By.XPATH, '//*[@data-testid="add-rule-button"]')


class TeachersPageLocators(MainPageLocators):
    ADD_TEACHER_BUTTON = (By.XPATH, '//*[@data-testid="add-teacher-button"]')
    TEACHERS_TABLE = (By.XPATH, '//*[@data-testid="teachers-table"]')
    SEARCH_TEACHERS_INPUT = (By.XPATH, '//*[@data-testid="search-teachers"]')


class LogsPageLocators(MainPageLocators):
    SEARCH_LOGS_INPUT = (By.XPATH, '//*[@data-testid="search-logs"]')
    LOGS_TABLE = (By.XPATH, '//*[@data-testid="logs-table"]')
    LOGS_FILTER = (By.XPATH, '//*[@data-testid="logs-filter-options"]')
