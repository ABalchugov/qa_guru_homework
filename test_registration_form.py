import time
import os
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec


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
            ec.visibility_of_element_located((By.XPATH, "//*[contains(text(), 'Level up your automation')]")))
        close_banner_btn = self.wait.until(ec.element_to_be_clickable(self.POPUP_CLOSE_BUTTON))
        close_banner_btn.click()

    def fill_first_name(self, name):
        field = self.driver.find_element(*self.FIRST_NAME_LOCATOR)
        field.send_keys(name)

    def fill_last_name(self, last_name):
        field = self.driver.find_element(*self.LAST_NAME_LOCATOR)
        field.send_keys(last_name)

    def fill_email(self,email):
        field = self.driver.find_element(*self.USER_EMAIL_LOCATOR)
        field.send_keys(email)

    def fill_mobile(self,mobile_number):
        field = self.driver.find_element(*self.MOBILE_LOCATOR)
        field.send_keys(mobile_number)

    def fill_current_address(self,current_address):
        field = self.driver.find_element(*self.CURRENT_ADDRESS_LOCATOR)
        field.send_keys(current_address)

    def click_on_gender(self, value):
        gender_wrapper = self.wait.until(ec.element_to_be_clickable(self.GENDERS_LOCATOR))
        gender = gender_wrapper.find_element(By.XPATH, f"//*[@value='{value}']")
        gender.click()

    def choose_date_of_birth(self, month, year, day):
        date_input = self.driver.find_element(*self.DATE_OF_BIRTH_LOCATOR)
        date_input.click()
        self.wait.until(ec.visibility_of_element_located((By.CLASS_NAME, "react-datepicker__month-container")))
        # Выбор месяца
        month_select = self.wait.until(ec.element_to_be_clickable((By.CLASS_NAME, "react-datepicker__month-select")))
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
        subjects_input = self.wait.until(ec.element_to_be_clickable(self.SUBJECTS_LOCATOR))
        subjects_input.send_keys(subject)
        subjects_input.send_keys(Keys.ENTER)

    def choose_hobbies(self, value):
        hobbies_wrapper = self.wait.until(ec.element_to_be_clickable(self.HOBBIES_LOCATOR))
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
        state_dropdown = self.wait.until(ec.element_to_be_clickable(self.STATE_LOCATOR))
        state_dropdown.click()
        state_wrapper = self.wait.until(ec.element_to_be_clickable((By.ID, "stateCity-wrapper")))
        state_option = state_wrapper.find_element(By.XPATH, f".//*[text()='{state}']")
        state_option.click()

    def choose_city(self, city):
        city_dropdown = self.wait.until(ec.element_to_be_clickable(self.CITY_LOCATOR))
        city_dropdown.click()
        city_wrapper = self.wait.until(ec.element_to_be_clickable((By.ID, "stateCity-wrapper")))
        city_option = city_wrapper.find_element(By.XPATH, f".//*[text()='{city}']")
        city_option.click()

    def click_submit_button(self):
        submit_button = self.driver.find_element(*self.SUBMIT_BUTTON_LOCATOR)
        self.driver.execute_script("arguments[0].click();", submit_button)

    # Тест формы со всеми заполненными полями и валидными данными
    def all_fields_valid(self):
        first_name = "John"
        last_name = "Wick"
        user_email = "JWick@someemail.com"
        gender = "Male"
        mobile = "8005553535"
        month_of_birth = 7
        day_of_birth = 20
        year_of_birth = 1994
        subject = "Maths"
        hobby = "Sports"
        picture_path = "test_image.jpg"
        current_address = "Ягодная, д.1"
        state = "NCR"
        city = "Gurgaon"

        try:
            self.set_up()
            time.sleep(2)
            self.close_popup()
            self.fill_first_name(first_name)
            self.fill_last_name(last_name)
            self.fill_email(user_email)
            time.sleep(2)
            self.click_on_gender(gender)
            self.fill_mobile(mobile)
            self.choose_date_of_birth(month_of_birth, year_of_birth,day_of_birth)
            self.choose_subjects(subject)
            self.choose_hobbies(hobby)
            time.sleep(2)
            self.picture_upload(picture_path)
            self.fill_current_address(current_address)
            self.scroll()
            self.choose_state(state)
            self.choose_city(city)
            time.sleep(2)
            self.click_submit_button()

            # Проверка открытия модального окна
            modal_title = self.wait.until(ec.visibility_of_element_located(self.MODAL_TITLE))
            assert modal_title.text == "Thanks for submitting the form", "Модальное окно не открылось"
            # Проверяем наличие валидных данных в таблице результатов
            result_table = self.driver.find_element(*self.RESULT_TABLE)
            assert first_name in result_table.text, f"Имя {first_name} не найдено в таблице результатов"
            assert last_name in result_table.text, f"Фамилия {last_name} не найдена в таблице результатов"
            assert user_email in result_table.text, f"Email {user_email} не найден в таблице результатов"
            assert gender in result_table.text, f"Пол {gender} не найден в таблице результатов"
            assert mobile in result_table.text, f"Телефон {mobile} не найден в таблице результатов"
            assert subject in result_table.text, f"Предмет {subject} не найден в таблице результатов"
            assert hobby in result_table.text, f"Хобби {hobby} не найдено в таблице результатов"
            assert picture_path in result_table.text, f"Файл {picture_path} не найден в таблице результатов"
            assert current_address in result_table.text, f"Адрес {current_address} не найден в таблице результатов"
            assert state in result_table.text, f"Адрес {state} не найден в таблице результатов"
            assert city in result_table.text, f"Адрес {city} не найден в таблице результатов"
            print("Все проверки успешно пройдены!")
            time.sleep(5)

        finally:
            self.tear_down()


test = TestRegistration()
test.all_fields_valid()
