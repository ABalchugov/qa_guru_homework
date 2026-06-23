import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.common.exceptions import NoSuchElementException, StaleElementReferenceException, TimeoutException


class TestSuite:
    FULL_NAME_LOCATOR = (By.ID, "userName")
    EMAIL_LOCATOR = (By.ID, "userEmail")
    CURRENT_ADDRESS_LOCATOR = (By.ID, "currentAddress")
    PERMANENT_ADDRESS_LOCATOR = (By.ID, "permanentAddress")
    SUBMIT_BUTTON_LOCATOR = (By.ID, "submit")
    RESULT_BOX_LOCATOR = (By.ID, "output")

    def __init__(self):
        self.driver = None
        self.wait = None

    def set_up(self):
        self.driver = webdriver.Chrome()
        self.wait = WebDriverWait(
            self.driver,
            timeout=10,
            poll_frequency=0.5,
            ignored_exceptions=[NoSuchElementException, StaleElementReferenceException]
        )
        self.driver.get("https://qa-guru.github.io/one-page-form/text-box.html")
        self.driver.maximize_window()
        self.driver.implicitly_wait(5)

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

    # Тест поля FullName
    def test_full_name(self):
        try:
            # Открытие страницы
            self.set_up()

            # Поиск элементов и заполнение полей
            # Находим поле Full Name по его ID и вводим текст
            self._fill_full_name_field("Александр Александров")

            # Находим поле Email по его ID и вводим текст
            self._fill_email_field("alexandr@example.com")

            # Находим кнопку Submit по ее ID и кликаем
            self._click_submit_button()

            # Проверка результата
            time.sleep(5)  # Пауза, чтобы увидеть результат отправки

            # Ожидание появления блока с результатами (id="output")
            result_box = self._wait_result_box()

            # Проверяем, что в блоке результата появился введенный текст
            assert "Александр Александров" in result_box.text
            print("Тест поля Full Name успешно пройден!")
        finally:
            test_suite.tear_down()

    # Негативный тест поля Email без @
    def test_email_negative(self):
        try:
            # Открытие страницы
            self.set_up()

            # Поиск элементов и заполнение полей
            # Находим поле Full Name по его ID и вводим текст
            self._fill_full_name_field("Александр Александров")

            # Находим поле Email по его ID и вводим текст
            self._fill_email_field("alexandrexample.com")

            # Находим кнопку Submit по ее ID и кликаем
            self._click_submit_button()

            # Проверка результата
            time.sleep(5)  # Пауза, чтобы увидеть результат отправки

            # Находим блок с отправленными данными
            result_box = None
            try:
                result_box = self._wait_result_box()
            except TimeoutException:
                pass

            # Проверяем, что в блоке результата появился введенный текст
            assert result_box is None
            print("Негативный тест поля Email успешно пройден!")
        finally:
            test_suite.tear_down()

    # Тест поля Current Address
    def test_current_address(self):
        try:
            # Открытие страницы
            self.set_up()

            # Поиск элементов и заполнение полей
            # Находим поле Full Name по его ID и вводим текст
            self._fill_full_name_field("Александр Александров")

            # Находим поле Email по его ID и вводим текст
            self._fill_email_field("alexandr@example.com")

            # Находим поле Current Address по его ID и вводим текст
            self._fill_current_address_field("Москва, Петровка, 38")

            # Находим кнопку Submit по ее ID и кликаем
            self._click_submit_button()
            # Проверка результата
            time.sleep(5)  # Пауза, чтобы увидеть результат отправки

            # Находим блок с отправленными данными
            result_box = self._wait_result_box()

            # Проверяем, что в блоке результата появился введенный текст
            assert "Москва, Петровка, 38" in result_box.text
            print("Тест поля Current Address успешно пройден!")
        finally:
            test_suite.tear_down()

    # Тест поля Permanent Address
    def test_permanent_address(self):
        try:
            # Открытие страницы
            self.set_up()

            # Поиск элементов и заполнение полей
            # Находим поле Full Name по его ID и вводим текст
            self._fill_full_name_field("Александр Александров")

            # Находим поле Email по его ID и вводим текст
            self._fill_email_field("alexandr@example.com")

            # Находим поле Permanent Address по его ID и вводим текст
            self._fill_permanent_address_field("Москва, Б. Лубянка, 2")

            # Находим кнопку Submit по ее ID и кликаем
            self._click_submit_button()

            # Проверка результата
            time.sleep(5)  # Пауза, чтобы увидеть результат отправки

            # Находим блок с отправленными данными
            result_box = self._wait_result_box()

            # Проверяем, что в блоке результата появился введенный текст
            assert "Москва, Б. Лубянка, 2" in result_box.text
            print("Тест поля Permanent Address успешно пройден!")
        finally:
            test_suite.tear_down()


test_suite = TestSuite()

test_suite.test_full_name()
test_suite.test_email_negative()
test_suite.test_current_address()
test_suite.test_permanent_address()
