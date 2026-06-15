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
    GENDERS_LOCATOR = (By.ID, "genterWrapper")
    MOBILE_LOCATOR = (By.ID, "userNumber")
    DATE_OF_BIRTH_LOCATOR = (By.ID, "dateOfBirthInput")
    SUBJECTS_LOCATOR = (By.ID, "subjectsInput")
    HOBBIES_LOCATOR = (By.ID, "hobbiesWrapper")
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

    def _find_input(self, locator):
        field = self.driver.find_element(*locator)
        return field

    def _fill_input(self, field, key):
        field.send_keys(key)

    def click_on_gender(self, value):
        gender_wrapper = self.wait.until(EC.element_to_be_clickable(self.GENDERS_LOCATOR))
        gender = gender_wrapper.find_element(By.XPATH, f"//*[@value='{value}']")
        gender.click()

    def choose_date_of_birth(self, month, year, day):
        date_input = self.driver.find_element(*self.DATE_OF_BIRTH_LOCATOR)
        date_input.click()
        self.wait.until(EC.visibility_of_element_located((By.CLASS_NAME, "react-datepicker__month-container")))
        # Выбор месяца
        month_select = self.wait.until(EC.element_to_be_clickable((By.CLASS_NAME, "react-datepicker__month-select")))
        month_select.click()
        month_select.find_element(By.XPATH, f"//option[@value='{month - 1}']").click()
        # Выбор года
        year_select = self.driver.find_element(By.CLASS_NAME, "react-datepicker__year-select")
        year_select.click()
        year_select.find_element(By.XPATH, f"//option[@value='{year}']").click()
        # Выбор дня
        day_element = self.driver.find_element(By.CSS_SELECTOR,
                                               f".react-datepicker__day--0{day}:not(.react-datepicker__day--outside-month)")
        day_element.click()

    def choose_subjects(self, subject):
        subjects_input = self.wait.until(EC.element_to_be_clickable(self.SUBJECTS_LOCATOR))
        subjects_input.send_keys(subject)
        subjects_input.send_keys(Keys.ENTER)

    def choose_hobbies(self, value):
        hobbies_wrapper = self.wait.until(EC.element_to_be_clickable(self.HOBBIES_LOCATOR))
        hobby = hobbies_wrapper.find_element(By.XPATH, f"//*[@value='{value}']")
        hobby.click()

    def picture_upload(self, path):
        temp_file_path = os.path.abspath(path)
        with open(temp_file_path, "w") as f:
            f.write("fake image data")

        upload_input = self.driver.find_element(*self.PICTURE_LOCATOR)
        upload_input.send_keys(temp_file_path)

    def scroll(self):
        self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        self.driver.execute_script("document.getElementsByTagName('footer')[0].style.display='none';")

    def choose_state(self, state):
        state_dropdown = self.wait.until(EC.element_to_be_clickable(self.STATE_LOCATOR))
        state_dropdown.click()
        state_wrapper = self.wait.until(EC.element_to_be_clickable((By.ID, "stateCity-wrapper")))
        state_option = state_wrapper.find_element(By.XPATH, f".//*[text()='{state}']")
        state_option.click()

    def choose_city(self, city):
        city_dropdown = self.wait.until(EC.element_to_be_clickable(self.CITY_LOCATOR))
        city_dropdown.click()
        city_wrapper = self.wait.until(EC.element_to_be_clickable((By.ID, "stateCity-wrapper")))
        city_option = city_wrapper.find_element(By.XPATH, f".//*[text()='{city}']")
        city_option.click()

    def push_submit_button(self):
        submit_button = self.driver.find_element(*self.SUBMIT_BUTTON_LOCATOR)
        self.driver.execute_script("arguments[0].click();", submit_button)

    # Тест формы со всеми заполненными полями и валидными данными
    def all_fields_valid(self):
        expected_values = {
            "first_name": "John",
            "last_name": "Wick",
            "user_email": "JWick@someemail.com",
            "gender": "Male",
            "mobile": "8005553535",
            "month_of_birth": 7,
            "day_of_birth": 20,
            "year_of_birth": 1994,
            "subject": "Maths",
            "hobby": "Sports",
            "picture_path": "test_image.jpg",
            "current_address": "Ягодная, д.1",
            "state": "NCR",
            "city": "Gurgaon"
        }

        try:
            self.set_up()
            time.sleep(2)
            self.close_popup()
            self._fill_input(self._find_input(self.FIRST_NAME_LOCATOR), expected_values["first_name"])
            self._fill_input(self._find_input(self.LAST_NAME_LOCATOR), expected_values["last_name"])
            self._fill_input(self._find_input(self.USER_EMAIL_LOCATOR), expected_values["user_email"])
            time.sleep(2)
            self.click_on_gender(expected_values["gender"])
            self._fill_input(self._find_input(self.MOBILE_LOCATOR), expected_values["mobile"])
            self.choose_date_of_birth(expected_values["month_of_birth"], expected_values["year_of_birth"],
                                      expected_values["day_of_birth"])
            self.choose_subjects(expected_values["subject"])
            self.choose_hobbies(expected_values["hobby"])
            time.sleep(2)
            self.picture_upload(expected_values["picture_path"])
            self._fill_input(self._find_input(self.CURRENT_ADDRESS_LOCATOR), expected_values["current_address"])
            self.scroll()
            self.choose_state(expected_values["state"])
            self.choose_city(expected_values["city"])
            time.sleep(2)
            self.push_submit_button()

            # Проверка открытия модального окна
            modal_title = self.wait.until(EC.visibility_of_element_located(self.MODAL_TITLE))
            assert modal_title.text == "Thanks for submitting the form", "Модальное окно не открылось"
            # Проверяем наличие валидных данных в таблице результатов
            result_table = self.driver.find_element(*self.RESULT_TABLE)
            assert expected_values[
                       "first_name"] in result_table.text, f"Имя {expected_values["first_name"]} не найдено в таблице результатов"
            assert expected_values[
                       "last_name"] in result_table.text, f"Фамилия {expected_values["last_name"]} не найдена в таблице результатов"
            assert expected_values[
                       "user_email"] in result_table.text, f"Email {expected_values["user_email"]} не найден в таблице результатов"
            assert expected_values[
                       "gender"] in result_table.text, f"Пол {expected_values["gender"]} не найден в таблице результатов"
            assert expected_values[
                       "mobile"] in result_table.text, f"Телефон {expected_values["mobile"]} не найден в таблице результатов"
            assert expected_values[
                       "subject"] in result_table.text, f"Предмет {expected_values["subject"]} не найден в таблице результатов"
            assert expected_values[
                       "hobby"] in result_table.text, f"Хобби {expected_values["hobby"]} не найдено в таблице результатов"
            assert expected_values[
                       "picture_path"] in result_table.text, f"Файл {expected_values["picture_path"]} не найден в таблице результатов"
            assert expected_values[
                       "current_address"] in result_table.text, f"Адрес {expected_values["current_address"]} не найден в таблице результатов"
            assert expected_values[
                       "state"] in result_table.text, f"Адрес {expected_values["state"]} не найден в таблице результатов"
            assert expected_values[
                       "city"] in result_table.text, f"Адрес {expected_values["city"]} не найден в таблице результатов"
            print("Все проверки успешно пройдены!")
            time.sleep(5)

        finally:
            self.tear_down()


test = TestRegistration()
test.all_fields_valid()
