from POM_homework.refactored_test_form import test_form_po
from test_data import UserData


class TestFormTestSuite:

    def __init__(self):
        self.test_form = None

    def setup(self):
        self.test_form = test_form_po.TestFormPO("https://qa-guru.github.io/one-page-form/text-box.html")
        self.test_form.setup()

    def tear_down(self):
        self.test_form.tear_down()

    def test_full_name(self):
        try:
            user = UserData()
            self.setup()
            self.test_form.fill_form(user.name, user.email)
            self.test_form.assert_result_box_is_displayed()
            self.test_form.assert_result_box_content(user.name, user.email)
        finally:
            self.tear_down()

    # Негативный тест поля Email без @
    def test_email_negative(self):
        try:
            user = UserData(email="alexandrexample.com")
            self.setup()
            self.test_form.fill_form(user.name, user.email)
            self.test_form.assert_result_box_is_not_displayed()
        finally:
            self.tear_down()

    # Тест поля Current Address
    def test_current_address(self):
        try:
            user = UserData(current_address="Москва, Петровка, 38")
            self.setup()
            self.test_form.fill_form(user.name, user.email, user.current_address)
            self.test_form.assert_result_box_is_displayed()
            self.test_form.assert_result_box_content(user.name, user.email, user.current_address)
        finally:
            self.tear_down()

    # Тест поля Permanent Address
    def test_permanent_address(self):
        try:
            user = UserData(permanent_address="Москва, Б. Лубянка, 2")
            self.setup()
            self.test_form.fill_form(user.name, user.email, user.current_address, user.permanent_address)
            self.test_form.assert_result_box_is_displayed()
            self.test_form.assert_result_box_content(user.name, user.email, user.current_address,
                                                     user.permanent_address)
        finally:
            self.tear_down()


test_form_suite = TestFormTestSuite()
test_form_suite.test_full_name()
test_form_suite.test_email_negative()
test_form_suite.test_current_address()
test_form_suite.test_permanent_address()
