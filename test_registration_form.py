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

    def __init__(self):
        self.driver = None
