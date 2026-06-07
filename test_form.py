import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException, StaleElementReferenceException


class TestSuite:
    FULL_NAME_LOCATOR = (By.ID, "userName")
    EMAIL_LOCATOR = (By.ID, "userEmail")
    CURRENT_ADDRESS_LOCATOR = (By.ID, "currentAddress")
    PERMANENT_ADDRESS_LOCATOR = (By.ID, "permanentAddress")
    SUBMIT_BUTTON_LOCATOR = (By.ID, "submit")
    RESULT_BOX_LOCATOR = (By.ID, "output")

    def __init__(self):
        self.driver = None

    def set_up(self):
        self.driver = webdriver.Chrome()
        self.driver.get("https://qa-guru.github.io/one-page-form/text-box.html")
        self.driver.maximize_window()
        self.driver.implicitly_wait(5)

    def tear_down(self):
        self.driver.quit()

    def _find_field_and_send_keys(self, locator, key):
        field = self.driver.find_element(*locator)
        field.send_keys(key)

    def _push_submit_button(self):
        submit_button = self.driver.find_element(*self.SUBMIT_BUTTON_LOCATOR)
        submit_button.click()

    def _wait_result_box(self):
        wait = WebDriverWait(
            self.driver,
            timeout=10,
            poll_frequency=0.5,
            ignored_exceptions=[NoSuchElementException, StaleElementReferenceException]
        )

        return wait.until(EC.visibility_of_element_located(self.RESULT_BOX_LOCATOR))

    # Тест поля FullName
    def test_full_name(self):
        try:
            # Открытие страницы
            self.set_up()

            # Поиск элементов и заполнение полей
            # Находим поле Full Name по его ID и вводим текст
            self._find_field_and_send_keys(self.FULL_NAME_LOCATOR, "Александр Александров")

            # Находим поле Email по его ID и вводим текст
            self._find_field_and_send_keys(self.EMAIL_LOCATOR, "alexandr@example.com")

            # Находим кнопку Submit по ее ID и кликаем
            self._push_submit_button()

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
            self._find_field_and_send_keys(self.FULL_NAME_LOCATOR, "Александр Александров")

            # Находим поле Email по его ID и вводим текст
            self._find_field_and_send_keys(self.EMAIL_LOCATOR, "alexandrexample.com")

            # Находим кнопку Submit по ее ID и кликаем
            self._push_submit_button()

            # Проверка результата
            time.sleep(5)  # Пауза, чтобы увидеть результат отправки

            # Находим блок с отправленными данными
            result_box = self._wait_result_box()

            # Проверяем, что в блоке результата появился введенный текст
            assert "alexandrexample.com" not in result_box.text
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
            self._find_field_and_send_keys(self.FULL_NAME_LOCATOR, "Александр Александров")

            # Находим поле Email по его ID и вводим текст
            self._find_field_and_send_keys(self.EMAIL_LOCATOR, "alexandr@example.com")

            # Находим поле Current Address по его ID и вводим текст
            self._find_field_and_send_keys(self.CURRENT_ADDRESS_LOCATOR, "Москва, Петровка, 38")

            # Находим кнопку Submit по ее ID и кликаем
            self._push_submit_button()

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
            self._find_field_and_send_keys(self.FULL_NAME_LOCATOR, "Александр Александров")

            # Находим поле Email по его ID и вводим текст
            self._find_field_and_send_keys(self.EMAIL_LOCATOR, "alexandr@example.com")

            # Находим поле Permanent Address по его ID и вводим текст
            self._find_field_and_send_keys(self.PERMANENT_ADDRESS_LOCATOR, "Москва, Б. Лубянка, 2")

            # Находим кнопку Submit по ее ID и кликаем
            self._push_submit_button()

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
