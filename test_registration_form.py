import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException, StaleElementReferenceException


class TestRegistration:
    FIRST_NAME_LOCATOR = (By.ID, "firstName")
    LAST_NAME_LOCATOR = (By.ID, "lastName")
    USER_EMAIL_LOCATOR = (By.ID, "userEmail")
    GENDER_MALE_LOCATOR = (By.CSS_SELECTOR, "label[for='gender-radio-1']")
    GENDER_FEMALE_LOCATOR = (By.CSS_SELECTOR, "label[for='gender-radio-2']")
    GENDER_OTHER_LOCATOR = (By.CSS_SELECTOR, "label[for='gender-radio-3']")
    MOBILE_LOCATOR = (By.ID, "userNumber")
    DATE_OF_BIRTH_LOCATOR = (By.ID, "dateOfBirthInput")
    SUBJECTS_LOCATOR = (By.ID, "subjectsInput")
    HOBBIES_SPORTS_LOCATOR = (By.CSS_SELECTOR, "label[for='hobbies-checkbox-1']")
    HOBBIES_READING_LOCATOR = (By.CSS_SELECTOR, "label[for='hobbies-checkbox-2']")
    HOBBIES_MUSIC_LOCATOR = (By.CSS_SELECTOR, "label[for='hobbies-checkbox-3']")
    PICTURE_LOCATOR = (By.ID, "uploadPicture")
    CURRENT_ADDRESS_LOCATOR = (By.ID, "currentAddress")
    STATE_LOCATOR = (By.ID, "state")
    CITY_LOCATOR = (By.ID, "city")
    SUBMIT_BUTTON_LOCATOR = (By.ID, "submit")
    POPUP_CLOSE_BUTTON = (By.XPATH, """//*[@id="fixedban"]/div/div/button""")

    def __init__(self):
        self.driver = None
        self.wait = None

    def set_up(self):
        self.driver = webdriver.Chrome()
        self.driver.get("https://qa-guru.github.io/one-page-form/automation-practice-form.html")
        self.driver.maximize_window()
        self.wait = WebDriverWait(self.driver, 5)


    def tear_down(self):
        self.driver.quit()

    def _find_field_and_send_keys(self, locator, key):
        field = self.driver.find_element(*locator)
        field.send_keys(key)

    def click_on_gender(self, locator):
        gender_label = self.wait.until(EC.element_to_be_clickable(locator))
        gender_label.click()

    def _push_submit_button(self):
        submit_button = self.driver.find_element(*self.SUBMIT_BUTTON_LOCATOR)
        submit_button.click()

    def close_popup(self):
        self.wait.until(EC.visibility_of_element_located((By.XPATH, "//*[contains(text(), 'Level up your automation')]")))
        close_banner_btn = self.wait.until(EC.element_to_be_clickable(self.POPUP_CLOSE_BUTTON))
        close_banner_btn.click()

    #Тест формы со всеми заполненными полями и валидными данными
    def all_fields_valid(self):
        try:
            self.set_up()
            time.sleep(2)
            self.close_popup()
            self._find_field_and_send_keys(self.FIRST_NAME_LOCATOR, "John")
            self._find_field_and_send_keys(self.LAST_NAME_LOCATOR, "Wick")
            self._find_field_and_send_keys(self.USER_EMAIL_LOCATOR, "JWick@gmail.com")
            self.click_on_gender(self.GENDER_MALE_LOCATOR)
            self._find_field_and_send_keys(self.MOBILE_LOCATOR, "8005553535")
            time.sleep(5)

        finally:
            self.tear_down()

test = TestRegistration()
test.all_fields_valid()