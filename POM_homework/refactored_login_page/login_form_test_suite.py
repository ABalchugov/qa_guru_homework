import login_form_po


class LoginFormTestSuite:
    def __init__(self):
        self.login_form = None

    def setup(self):
        self.login_form = login_form_po.LoginFormPO(
            "https://qa-guru.github.io/one-page-form/login.html")
        self.login_form.setup()

    def tear_down(self):
        self.login_form.tear_down()

    # Тест логина с валидной парой логин-пароль
    def valid_login_and_password(self):
        try:
            # Открытие страницы
            self.setup()
            # Заполнение полей
            self.login_form.fill_form("user1", "password1")
            # Проверка результата
            self.login_form.assert_welcome_msg_is_displayed()
        finally:
            self.tear_down()

    # Тест логина с невалидной парой логин-пароль
    def invalid_login_and_password(self):
        try:
            # Открытие страницы
            self.setup()
            # Заполнение полей
            self.login_form.fill_form("user2", "password2")
            # Проверка того, что поле отобразилось
            self.login_form.assert_error_msg_is_displayed()
            # Проверка того, что сообщение об ошибке соответствует ожидаемому
            self.login_form.assert_error_msg_content("Wrong login or password")
        finally:
            self.tear_down()

    # Тест на короткий логин
    def short_login(self):
        try:
            # Открытие страницы
            self.setup()
            # Заполнение полей
            self.login_form.fill_form("a", "password2")
            # Проверка того, что поле отобразилось
            self.login_form.assert_error_msg_is_displayed()
            # Проверка того, что сообщение об ошибке соответствует ожидаемому
            self.login_form.assert_error_msg_content("Login must be at least 3 characters")
        finally:
            self.tear_down()

    # Тест на короткий пароль
    def short_password(self):
        try:
            # Открытие страницы
            self.setup()
            # Заполнение полей
            self.login_form.fill_form("user1", "a")
            # Проверка того, что поле отобразилось
            self.login_form.assert_error_msg_is_displayed()
            # Проверка того, что сообщение об ошибке соответствует ожидаемому
            self.login_form.assert_error_msg_content("Password must be at least 6 characters")
        finally:
            self.tear_down()


test_suite = LoginFormTestSuite()

test_suite.valid_login_and_password()
test_suite.invalid_login_and_password()
test_suite.short_login()
test_suite.short_password()
