
import time
from selenium import webdriver
from selenium.webdriver.common.by import By

class TestSuite:
    full_name_locator = (By.ID, "userName")
    email_locator = (By.ID, "userEmail")
    current_address_locator = (By.ID, "currentAddress")
    permanent_address_locator = (By.ID, "permanentAddress")
    submit_button_locator = (By.ID, "submit")
    result_box_locator = (By.ID, "output")

    def __init__(self):
        self.driver = webdriver.Chrome()

    def set_up(self):
        self.driver.get("https://qa-guru.github.io/one-page-form/text-box.html")
        self.driver.maximize_window()
        time.sleep(5)

    def tear_down(self):
        self.driver.quit()

    # Тест поля FullName
    def test_full_name(self):

        try:
            # Открытие страницы
            self.set_up()

            # Поиск элементов и заполнение полей
            full_name_field = self.driver.find_element(*self.full_name_locator)
            full_name_field.send_keys("Александр Александров")

            # Находим поле Email по его ID и вводим текст
            email_field = self.driver.find_element(*self.email_locator)
            email_field.send_keys("alexandr@example.com")

            # Находим кнопку Submit по ее ID и кликаем
            submit_button = self.driver.find_element(*self.submit_button_locator)
            submit_button.click()

            # Проверка результата
            time.sleep(5)  # Пауза, чтобы увидеть результат отправки

            # Находим блок с отправленными данными
            result_box = self.driver.find_element(*self.result_box_locator)

            # Проверяем, что в блоке результата появился введенный текст
            assert "Александр Александров" in result_box.text
            print("Тест поля Full Name успешно пройден!")

        finally:
            pass

    # Негативный тест поля Email без @
    def test_email_negative(self):

        try:
            # Открытие страницы
            self.set_up()

            # Поиск элементов и заполнение полей
            # Находим поле Full Name по его ID и вводим текст
            full_name_field = self.driver.find_element(*self.full_name_locator)
            full_name_field.send_keys("Александр Александров")

            # Находим поле Email по его ID и вводим текст
            email_field = self.driver.find_element(*self.email_locator)
            email_field.send_keys("alexandrexample.com")

            # Находим кнопку Submit по ее ID и кликаем
            submit_button = self.driver.find_element(*self.submit_button_locator)
            submit_button.click()

            # Проверка результата
            time.sleep(5)  # Пауза, чтобы увидеть результат отправки

            # Находим блок с отправленными данными
            result_box = self.driver.find_element(*self.result_box_locator)

            # Проверяем, что в блоке результата появился введенный текст
            assert "alexandrexample.com" not in result_box.text
            print("Негативный тест поля Email успешно пройден!")

        finally:
            pass

    # Тест поля Current Address
    def test_current_address(self):

        try:
            # Открытие страницы
            self.set_up()

            # Поиск элементов и заполнение полей
            # Находим поле Full Name по его ID и вводим текст
            full_name_field = self.driver.find_element(*self.full_name_locator)
            full_name_field.send_keys("Александр Александров")

            # Находим поле Email по его ID и вводим текст
            email_field = self.driver.find_element(*self.email_locator)
            email_field.send_keys("alexandr@example.com")

            # Находим поле Current Address по его ID и вводим текст
            current_address_field = self.driver.find_element(*self.current_address_locator)
            current_address_field.send_keys("Москва, Петровка, 38")

            # Находим кнопку Submit по ее ID и кликаем
            submit_button = self.driver.find_element(*self.submit_button_locator)
            submit_button.click()

            # Проверка результата
            time.sleep(5)  # Пауза, чтобы увидеть результат отправки

            # Находим блок с отправленными данными
            result_box = self.driver.find_element(*self.result_box_locator)

            # Проверяем, что в блоке результата появился введенный текст
            assert "Москва, Петровка, 38" in result_box.text
            print("Тест поля Current Address успешно пройден!")

        finally:
            pass

    # Тест поля Permanent Address
    def test_permanent_address(self):

        try:
            # Открытие страницы
            self.set_up()

            # Поиск элементов и заполнение полей
            # Находим поле Full Name по его ID и вводим текст
            full_name_field = self.driver.find_element(*self.full_name_locator)
            full_name_field.send_keys("Александр Александров")

            # Находим поле Email по его ID и вводим текст
            email_field = self.driver.find_element(*self.email_locator)
            email_field.send_keys("alexandr@example.com")

            # Находим поле Permanent Address по его ID и вводим текст
            permanent_address_field = self.driver.find_element(*self.permanent_address_locator)
            permanent_address_field.send_keys("Москва, Б. Лубянка, 2")

            # Находим кнопку Submit по ее ID и кликаем
            submit_button = self.driver.find_element(*self.submit_button_locator)
            submit_button.click()

            # Проверка результата
            time.sleep(5)  # Пауза, чтобы увидеть результат отправки

            # Находим блок с отправленными данными
            result_box = self.driver.find_element(*self.result_box_locator)

            # Проверяем, что в блоке результата появился введенный текст
            assert "Москва, Б. Лубянка, 2" in result_box.text
            print("Тест поля Permanent Address успешно пройден!")

        finally:
            pass


test_suite = TestSuite()

test_suite.test_full_name()
test_suite.test_email_negative()
test_suite.test_current_address()
test_suite.test_permanent_address()
test_suite.tear_down()