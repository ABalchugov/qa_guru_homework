
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

    def _find_field_and_send_keys(self, locator, key):
        field = self.driver.find_element(*locator)
        field.send_keys(key)

    def _push_submit_button(self):
        submit_button = self.driver.find_element(*self.submit_button_locator)
        submit_button.click()

    def _find_result_box(self):
        return self.driver.find_element(*self.result_box_locator)


    # Тест поля FullName
    def test_full_name(self):

        try:
            # Открытие страницы
            self.set_up()

            # Поиск элементов и заполнение полей
            # Находим поле Full Name по его ID и вводим текст
            self._find_field_and_send_keys(self.full_name_locator, "Александр Александров")

            # Находим поле Email по его ID и вводим текст
            self._find_field_and_send_keys(self.email_locator, "alexandr@example.com")

            # Находим кнопку Submit по ее ID и кликаем
            self._push_submit_button()

            # Проверка результата
            time.sleep(5)  # Пауза, чтобы увидеть результат отправки

            # Находим блок с отправленными данными
            result_box = self._find_result_box()

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
            self._find_field_and_send_keys(self.full_name_locator, "Александр Александров")

            # Находим поле Email по его ID и вводим текст
            self._find_field_and_send_keys(self.email_locator, "alexandrexample.com")

            # Находим кнопку Submit по ее ID и кликаем
            self._push_submit_button()

            # Проверка результата
            time.sleep(5)  # Пауза, чтобы увидеть результат отправки

            # Находим блок с отправленными данными
            result_box = self._find_result_box()

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
            self._find_field_and_send_keys(self.full_name_locator, "Александр Александров")

            # Находим поле Email по его ID и вводим текст
            self._find_field_and_send_keys(self.email_locator, "alexandr@example.com")

            # Находим поле Current Address по его ID и вводим текст
            self._find_field_and_send_keys(self.current_address_locator, "Москва, Петровка, 38")

            # Находим кнопку Submit по ее ID и кликаем
            self._push_submit_button()

            # Проверка результата
            time.sleep(5)  # Пауза, чтобы увидеть результат отправки

            # Находим блок с отправленными данными
            result_box = self._find_result_box()

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
            self._find_field_and_send_keys(self.full_name_locator, "Александр Александров")

            # Находим поле Email по его ID и вводим текст
            self._find_field_and_send_keys(self.email_locator, "alexandr@example.com")

            # Находим поле Permanent Address по его ID и вводим текст
            self._find_field_and_send_keys(self.permanent_address_locator, "Москва, Б. Лубянка, 2")

            # Находим кнопку Submit по ее ID и кликаем
            self._push_submit_button()

            # Проверка результата
            time.sleep(5)  # Пауза, чтобы увидеть результат отправки

            # Находим блок с отправленными данными
            result_box = self._find_result_box()

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
