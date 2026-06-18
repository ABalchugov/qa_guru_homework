from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec


class LoginFormPO:
    LOGIN_LOCATOR = (By.ID, "login-input")
    PASSWORD_LOCATOR = (By.ID, "password-input")
    LOGIN_BUTTON_LOCATOR = (By.ID, "submit-button")
    ERROR_MESSAGE_LOCATOR = (By.ID, "error-message")
    WELCOME_MESSAGE_LOCATOR = (By.ID, "welcome-message")
    LOGOUT_BUTTON_LOCATOR = (By.ID, "logout-button")

    def __init__(self, url):
        self.driver = None
        self.wait = None
        self.url = url

    def setup(self):
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait = 5
        self.driver.maximize_window()
        self.wait = WebDriverWait(self.driver, 5)
        self.driver.get(self.url)

    def tear_down(self):
        self.driver.quit()

    def _find_field_and_send_keys(self, locator, key):
        field = self.driver.find_element(*locator)
        field.send_keys(key)

    def _push_login_button(self):
        login_button = self.driver.find_element(*self.LOGIN_BUTTON_LOCATOR)
        login_button.click()

    def fill_form(self, login, password):
        self._find_field_and_send_keys(self.LOGIN_LOCATOR, login)
        self._find_field_and_send_keys(self.PASSWORD_LOCATOR, password)
        self._push_login_button()

    def assert_welcome_msg_is_displayed(self):
        result_form = self.wait.until(ec.visibility_of_element_located(self.WELCOME_MESSAGE_LOCATOR))
        assert result_form.is_displayed(), "Сообщение не отобразилось"

    def assert_error_msg_is_displayed(self):
        result_form = self.wait.until(ec.visibility_of_element_located(self.ERROR_MESSAGE_LOCATOR))
        assert result_form.is_displayed(), "Сообщение не отобразилось"

    def assert_error_msg_content(self, message):
        has_message = self.wait.until(ec.text_to_be_present_in_element(self.ERROR_MESSAGE_LOCATOR, message))
        assert has_message, "Сообщение не соответствует ожидаемому"
