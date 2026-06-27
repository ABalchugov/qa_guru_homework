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

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 5)

    def fill_login_field(self, login):
        field = self.driver.find_element(*self.LOGIN_LOCATOR)
        field.send_keys(login)

    def fill_password_field(self, password):
        field = self.driver.find_element(*self.PASSWORD_LOCATOR)
        field.send_keys(password)

    def click_login_button(self):
        login_button = self.driver.find_element(*self.LOGIN_BUTTON_LOCATOR)
        login_button.click()

    def fill_form(self, login, password):
        self.fill_login_field(login)
        self.fill_password_field(password)
        self.click_login_button()

    def assert_welcome_msg_is_displayed(self):
        result_form = self.wait.until(ec.visibility_of_element_located(self.WELCOME_MESSAGE_LOCATOR))
        assert result_form.is_displayed(), "Сообщение не отобразилось"

    def assert_error_msg_is_displayed(self):
        result_form = self.wait.until(ec.visibility_of_element_located(self.ERROR_MESSAGE_LOCATOR))
        assert result_form.is_displayed(), "Сообщение не отобразилось"

    def assert_error_msg_content(self, message):
        has_message = self.wait.until(ec.text_to_be_present_in_element(self.ERROR_MESSAGE_LOCATOR, message))
        assert has_message, "Сообщение не соответствует ожидаемому"
