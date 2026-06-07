import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException, StaleElementReferenceException


class TestSuite:
    LOGIN_LOCATOR = (By.ID, "login-input")
    PASSWORD_LOCATOR = (By.ID, "password-input")
    LOGIN_BUTTON_LOCATOR = (By.ID, "submit-button")
    ERROR_MESSAGE_LOCATOR = (By.ID, "error-message")
    WELCOME_MESSAGE_LOCATOR = (By.ID, "welcome-message")
    LOGOUT_BUTTON_LOCATOR = (By.ID, "logout-button")

    def __init__(self):
        self.driver = None

    def set_up(self):
        self.driver = webdriver.Chrome()
        self.driver.get("https://qa-guru.github.io/one-page-form/login.html")
        self.driver.maximize_window()
        self.driver.implicitly_wait(5)

    def tear_down(self):
        self.driver.quit()

    def _find_field_and_send_keys(self, locator, key):
        field = self.driver.find_element(*locator)
        field.send_keys(key)

    def _push_login_button(self):
        login_button = self.driver.find_element(*self.LOGIN_BUTTON_LOCATOR)
        login_button.click()

    # Тест логина с валидной парой логин-пароль
    def valid_login_and_password(self):
        try:
            # Открытие страницы
            self.set_up()

            # Поиск элементов и заполнение полей
            # Находим поле Логин по его ID и вводим текст
            self._find_field_and_send_keys(self.LOGIN_LOCATOR, "user1")

            # Находим поле Пароль по его ID и вводим текст
            self._find_field_and_send_keys(self.PASSWORD_LOCATOR, "password1")

            time.sleep(5)

            # Находим кнопку Логин по ее ID и кликаем
            self._push_login_button()

            # Проверка результата
            time.sleep(5)  # Пауза, чтобы увидеть результат отправки

            # Находим блок с отправленными данными
            wait = WebDriverWait(
                self.driver,
                timeout=10,
                poll_frequency=0.5,
                ignored_exceptions=[NoSuchElementException, StaleElementReferenceException]
            )

            result_box = wait.until(EC.visibility_of_element_located(self.WELCOME_MESSAGE_LOCATOR))

            # Проверяем, что в блоке результата появился введенный текст
            assert "Welcome, user1!" in result_box.text
            print("Тест формы авторизации с валидной парой логин-пароль успешно пройден!")
        finally:
            self.tear_down()

    # Тест логина с невалидной парой логин-пароль
    def invalid_login_and_password(self):
        try:
            # Открытие страницы
            self.set_up()

            # Поиск элементов и заполнение полей
            # Находим поле Логин по его ID и вводим текст
            self._find_field_and_send_keys(self.LOGIN_LOCATOR, "user")

            # Находим поле Пароль по его ID и вводим текст
            self._find_field_and_send_keys(self.PASSWORD_LOCATOR, "password")

            time.sleep(5)

            # Находим кнопку Логин по ее ID и кликаем
            self._push_login_button()

            # Проверка результата
            time.sleep(5)  # Пауза, чтобы увидеть результат отправки

            # Находим блок с отправленными данными
            result_box = self.driver.find_element(*self.ERROR_MESSAGE_LOCATOR)

            # Проверяем, что в блоке результата появился введенный текст
            assert "Wrong login or password" in result_box.text
            print("Тест формы авторизации с невалидной парой логин-пароль успешно пройден!")
        finally:
            self.tear_down()

    # Тест на короткий логин
    def short_login(self):
        try:
            # Открытие страницы
            self.set_up()

            # Поиск элементов и заполнение полей
            # Находим поле Логин по его ID и вводим текст
            self._find_field_and_send_keys(self.LOGIN_LOCATOR, "a")

            # Находим поле Пароль по его ID и вводим текст
            self._find_field_and_send_keys(self.PASSWORD_LOCATOR, "password1")

            time.sleep(5)

            # Находим кнопку Логин по ее ID и кликаем
            self._push_login_button()

            # Проверка результата
            time.sleep(5)  # Пауза, чтобы увидеть результат отправки

            # Находим блок с отправленными данными
            result_box = self.driver.find_element(*self.ERROR_MESSAGE_LOCATOR)

            # Проверяем, что в блоке результата появился введенный текст
            assert "Login must be at least 3 characters" in result_box.text
            print("Тест формы авторизации с коротким логином успешно пройден!")
        finally:
            self.tear_down()

    # Тест на короткий пароль
    def short_password(self):
        try:
            # Открытие страницы
            self.set_up()

            # Поиск элементов и заполнение полей
            # Находим поле Логин по его ID и вводим текст
            self._find_field_and_send_keys(self.LOGIN_LOCATOR, "user1")

            # Находим поле Пароль по его ID и вводим текст
            self._find_field_and_send_keys(self.PASSWORD_LOCATOR, "a")

            time.sleep(5)

            # Находим кнопку Логин по ее ID и кликаем
            self._push_login_button()

            # Проверка результата
            time.sleep(5)  # Пауза, чтобы увидеть результат отправки

            # Находим блок с отправленными данными
            result_box = self.driver.find_element(*self.ERROR_MESSAGE_LOCATOR)

            # Проверяем, что в блоке результата появился введенный текст
            assert "Password must be at least 6 characters" in result_box.text
            print("Тест формы авторизации с коротким паролем успешно пройден!")
        finally:
            self.tear_down()


test_suite = TestSuite()

test_suite.valid_login_and_password()
test_suite.invalid_login_and_password()
test_suite.short_login()
test_suite.short_password()
