import time
from selenium import webdriver
from selenium.webdriver.common.by import By

class TestSuite:
    LOGIN_LOCATOR = (By.ID, "login-input")
    PASSWORD_LOCATOR = (By.ID, "password-input")
    LOGIN_BUTTON_LOCATOR = (By.ID, "submit-button")
    ERROR_MESSAGE_LOCATOR = (By.ID, "error-message")
    WELCOME_MESSAGE_LOCATOR = (By.ID, "welcome-message")
    LOGOUT_BUTTON_LOCATOR = (By.ID, "logout-button")

    def __init__(self):
        self.driver = webdriver.Chrome()

    def set_up(self):
        self.driver.get("https://qa-guru.github.io/one-page-form/login.html")
        self.driver.maximize_window()
        time.sleep(5)

    def tear_down(self):
        self.driver.quit()

    def _find_field_and_send_keys(self, locator, key):
        field = self.driver.find_element(*locator)
        field.send_keys(key)

    def _push_login_button(self):
        login_button = self.driver.find_element(*self.LOGIN_BUTTON_LOCATOR)
        login_button.click()

    #Логин с валидной парой пароль-логин
    def login_positive(self):
        try:
            # Открытие страницы
            self.set_up()

            # Поиск элементов и заполнение полей
            # Находим поле Логин по его ID и вводим текст
            self._find_field_and_send_keys(self.LOGIN_LOCATOR, "user1")

            # Находим поле Пароль по его ID и вводим текст
            self._find_field_and_send_keys(self.PASSWORD_LOCATOR, "password1")

            # Находим кнопку Логин по ее ID и кликаем
            self._push_login_button()

            # Проверка результата
            time.sleep(5)  # Пауза, чтобы увидеть результат отправки

            # Находим блок с отправленными данными
            result_box = self.driver.find_element(*self.WELCOME_MESSAGE_LOCATOR)

            # Проверяем, что в блоке результата появился введенный текст
            assert "Welcome, user1!" in result_box.text
            print("Позитивный тест формы авторизации успешно пройден!")

        finally:
            pass

test_suite = TestSuite()

test_suite.login_positive()
test_suite.tear_down()