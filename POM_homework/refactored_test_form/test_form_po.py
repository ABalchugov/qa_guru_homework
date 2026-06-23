from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.common.exceptions import TimeoutException


class TestFormPO:
    FULL_NAME_LOCATOR = (By.ID, "userName")
    EMAIL_LOCATOR = (By.ID, "userEmail")
    CURRENT_ADDRESS_LOCATOR = (By.ID, "currentAddress")
    PERMANENT_ADDRESS_LOCATOR = (By.ID, "permanentAddress")
    SUBMIT_BUTTON_LOCATOR = (By.ID, "submit")
    RESULT_BOX_LOCATOR = (By.ID, "output")

    def __init__(self, url):
        self.driver = None
        self.wait = None
        self.url = url

    def setup(self):
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait = 5
        self.driver.maximize_window()
        self.wait = WebDriverWait(self.driver, 10)
        self.driver.get(self.url)

    def tear_down(self):
        self.driver.quit()

    def _fill_full_name_field(self, name):
        field = self.driver.find_element(*self.FULL_NAME_LOCATOR)
        field.send_keys(name)

    def _fill_email_field(self, email):
        field = self.driver.find_element(*self.EMAIL_LOCATOR)
        field.send_keys(email)

    def _fill_current_address_field(self, current_address):
        field = self.driver.find_element(*self.CURRENT_ADDRESS_LOCATOR)
        field.send_keys(current_address)

    def _fill_permanent_address_field(self, permanent_address):
        field = self.driver.find_element(*self.PERMANENT_ADDRESS_LOCATOR)
        field.send_keys(permanent_address)

    def _click_submit_button(self):
        submit_button = self.driver.find_element(*self.SUBMIT_BUTTON_LOCATOR)
        submit_button.click()

    def _wait_result_box(self):
        return self.wait.until(ec.visibility_of_element_located(self.RESULT_BOX_LOCATOR))

    def fill_form(self, name, email, current_address="", permanent_address=""):
        self._fill_full_name_field(name)
        self._fill_email_field(email)
        if current_address != "":
            self._fill_current_address_field(current_address)
        if permanent_address != "":
            self._fill_permanent_address_field(permanent_address)
        self._click_submit_button()

    def assert_result_box_is_displayed(self):
        result_box = None

        try:
            result_box = self._wait_result_box()
        except TimeoutException:
            pass
        assert result_box is not None, "Поле с результатом не отобразилось"

    def assert_result_box_is_not_displayed(self):
        result_box = None

        try:
            result_box = self._wait_result_box()
        except TimeoutException:
            pass
        assert result_box is None, "Поле с результатом отобразилось"

    def assert_result_box_content(self, name, email, current_address="", permanent_address=""):
        result_box = self._wait_result_box()
        assert name in result_box.text, "Поле 'Full Name' не соответствует ожидаемому"
        assert email in result_box.text, "Поле 'Email' не соответствует ожидаемому"
        if current_address != "":
            assert current_address in result_box.text, "Поле 'Current Address' не соответствует ожидаемому"
        if permanent_address != "":
            assert permanent_address in result_box.text, "Поле 'Permanent Address' не соответствует ожидаемому"
