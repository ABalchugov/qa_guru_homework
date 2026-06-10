import time
import os
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class TestRegistration:
    FIRST_NAME_LOCATOR = (By.ID, "firstName")
    LAST_NAME_LOCATOR = (By.ID, "lastName")
    USER_EMAIL_LOCATOR = (By.ID, "userEmail")
    GENDER_MALE_LOCATOR = (By.CSS_SELECTOR, "label[for='gender-radio-1']")
    GENDER_FEMALE_LOCATOR = (By.CSS_SELECTOR, "label[for='gender-radio-2']")
    GENDER_OTHER_LOCATOR = (By.CSS_SELECTOR, "label[for='gender-radio-3']")
    MOBILE_LOCATOR = (By.ID, "userNumber")
    DATE_OF_BIRTH_LOCATOR = (By.ID, "dateOfBirthInput")
    MONTHS_LOCATORS = {
        "January": (By.XPATH, "//option[@value='0']"),
        "February": (By.XPATH, "//option[@value='1']"),
        "March": (By.XPATH, "//option[@value='2']"),
        "April": (By.XPATH, "//option[@value='3']"),
        "May": (By.XPATH, "//option[@value='4']"),
        "June": (By.XPATH, "//option[@value='5']"),
        "July": (By.XPATH, "//option[@value='6']"),
        "August": (By.XPATH, "//option[@value='7']"),
        "September": (By.XPATH, "//option[@value='8']"),
        "October": (By.XPATH, "//option[@value='9']"),
        "November": (By.XPATH, "//option[@value='10']"),
        "December": (By.XPATH, "//option[@value='11']"),
    }
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
    MODAL_TITLE = (By.ID, "example-modal-sizes-title-lg")
    RESULT_TABLE = (By.CLASS_NAME, "table-responsive")

    def __init__(self):
        self.driver = None
        self.wait = None

    def set_up(self):
        self.driver = webdriver.Chrome()
        self.driver.get("https://qa-guru.github.io/one-page-form/automation-practice-form.html")
        self.driver.maximize_window()
        self.wait = WebDriverWait(self.driver, 5)

    def tear_down(self):
        if os.path.exists("test_image.jpg"):
            os.remove("test_image.jpg")
        self.driver.quit()

    def close_popup(self):
        self.wait.until(
            EC.visibility_of_element_located((By.XPATH, "//*[contains(text(), 'Level up your automation')]")))
        close_banner_btn = self.wait.until(EC.element_to_be_clickable(self.POPUP_CLOSE_BUTTON))
        close_banner_btn.click()

    def _find_field_and_send_keys(self, locator, key):
        field = self.driver.find_element(*locator)
        field.send_keys(key)

    def click_on_gender(self, locator):
        gender_label = self.wait.until(EC.element_to_be_clickable(locator))
        gender_label.click()

    def choose_date_of_birth(self, month, year, day):
        date_input = self.driver.find_element(*self.DATE_OF_BIRTH_LOCATOR)
        date_input.click()
        self.wait.until(EC.visibility_of_element_located((By.CLASS_NAME, "react-datepicker__month-container")))
        # Выбор месяца
        month_select = self.wait.until(EC.element_to_be_clickable((By.CLASS_NAME, "react-datepicker__month-select")))
        month_select.click()
        month_select.find_element(*self.MONTHS_LOCATORS[month]).click()
        # Выбор года
        year_select = self.driver.find_element(By.CLASS_NAME, "react-datepicker__year-select")
        year_select.click()
        year_select.find_element(By.XPATH, f"//option[@value='{year}']").click()
        # Выбор дня
        day_element = self.driver.find_element(By.CSS_SELECTOR, f".react-datepicker__day--{day}:not(.react-datepicker__day--outside-month)")
        day_element.click()

    def choose_subjects(self, subject):
        subjects_input = self.wait.until(EC.element_to_be_clickable(self.SUBJECTS_LOCATOR))
        subjects_input.send_keys(subject)
        subjects_input.send_keys(Keys.ENTER)

    def choose_hobbies(self, locator):
        hobby = self.wait.until(
            EC.element_to_be_clickable(locator)
        )
        hobby.click()

    def picture_upload(self):
        temp_file_path = os.path.abspath("test_image.jpg")
        with open(temp_file_path, "w") as f:
            f.write("fake image data")

        upload_input = self.driver.find_element(*self.PICTURE_LOCATOR)
        upload_input.send_keys(temp_file_path)

    def scroll(self):
        self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        self.driver.execute_script("document.getElementsByTagName('footer')[0].style.display='none';")

    def choose_state(self, state_id):
        state_dropdown = self.wait.until(EC.element_to_be_clickable(self.STATE_LOCATOR))
        state_dropdown.click()
        state_option = self.wait.until(
            EC.element_to_be_clickable((By.XPATH, f"""//*[@id="stateCity-wrapper"]/div[{state_id}]""")))
        state_option.click()

    def choose_city(self, city_id):
        city_dropdown = self.wait.until(EC.element_to_be_clickable(self.CITY_LOCATOR))
        city_dropdown.click()
        city_option = self.wait.until(
            EC.element_to_be_clickable((By.XPATH, f"""//*[@id="stateCity-wrapper"]/div[{city_id}]""")))
        city_option.click()

    def push_submit_button(self):
        submit_button = self.driver.find_element(*self.SUBMIT_BUTTON_LOCATOR)
        self.driver.execute_script("arguments[0].click();", submit_button)

    # Тест формы со всеми заполненными полями и валидными данными
    def all_fields_valid(self):
        try:
            self.set_up()
            time.sleep(2)
            self.close_popup()
            self._find_field_and_send_keys(self.FIRST_NAME_LOCATOR, "John")
            self._find_field_and_send_keys(self.LAST_NAME_LOCATOR, "Wick")
            self._find_field_and_send_keys(self.USER_EMAIL_LOCATOR, "JWick@someemail.com")
            time.sleep(2)
            self.click_on_gender(self.GENDER_MALE_LOCATOR)
            self._find_field_and_send_keys(self.MOBILE_LOCATOR, "8005553535")
            self.choose_date_of_birth("July", 1994, "020")
            self.choose_subjects("Maths")
            self.choose_subjects("Physics")
            self.choose_hobbies(self.HOBBIES_SPORTS_LOCATOR)
            time.sleep(2)
            self.picture_upload()
            self._find_field_and_send_keys(self.CURRENT_ADDRESS_LOCATOR, "Ягодная, д.1")
            self.scroll()
            self.choose_state(state_id=2)
            self.choose_city(city_id=3)
            time.sleep(2)
            self.push_submit_button()

            # Проверка открытия модального окна
            modal_title = self.wait.until(EC.visibility_of_element_located(self.MODAL_TITLE))
            assert modal_title.text == "Thanks for submitting the form", "Модальное окно не открылось"
            # Проверяем наличие валидных данных в таблице результатов
            result_table = self.driver.find_element(*self.RESULT_TABLE)
            assert "John" in result_table.text, "Имя 'John' не найдено в таблице результатов"
            assert "Wick" in result_table.text, "Фамилия 'Wick' не найдена в таблице результатов"
            assert "JWick@someemail.com" in result_table.text, "Email 'JWick@someemail.com' не найден в таблице результатов"
            assert "Male" in result_table.text, "Пол 'Male' не найден в таблице результатов"
            assert "8005553535" in result_table.text, "Телефон '8005553535' не найден в таблице результатов"
            assert "Maths" in result_table.text, "Предмет 'Maths' не найден в таблице результатов"
            assert "Physics" in result_table.text, "Предмет 'Physics' не найден в таблице результатов"
            assert "Sports" in result_table.text, "Хобби 'Sports' не найдено в таблице результатов"
            assert "test_image.jpg" in result_table.text, "Файл 'test_image.jpg' не найден в таблице результатов"
            assert "Ягодная, д.1" in result_table.text, "Адрес 'Ягодная, д.1' не найден в таблице результатов"
            print("✅ Все проверки успешно пройдены!")
            time.sleep(5)

        finally:
            self.tear_down()


test = TestRegistration()
test.all_fields_valid()
