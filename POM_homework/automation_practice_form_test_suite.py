import os
import automation_practice_form_po


class AutomationPracticeFormTestSuite:
    def __init__(self):
        self.automation_practice_form = None

    def setup(self):
        self.automation_practice_form = automation_practice_form_po.AutomationPracticeFormPO(
            "https://qa-guru.github.io/one-page-form/automation-practice-form.html")
        self.automation_practice_form.setup()
        self.tmp_file_name = self._create_tmp_file()

    def _create_tmp_file(self):
        file_path = os.path.abspath('test_file.jpg')
        with open(file_path, 'w') as file:
            file.write("Test")
        return file_path

    def test_form_positive01(self):
        test_suite.setup()
        self.automation_practice_form.fill_in_form(self.tmp_file_name, "Dmitry", "Bugaev", "bugaev@example.com", "Male",
                                                   "1234567890", ("1988", "4", "22"), ("Maths", "English"),
                                                   ("Sports", "Music"),
                                                   "г. Санкт-Петербург, ул. Невский проспект, д 101", "NCR", "Noida")
        self.automation_practice_form.assert_result_is_displayed()
        self.automation_practice_form.assert_result_data(self.tmp_file_name, "Dmitry", "Bugaev", "bugaev@example.com", "Male",
                                                  "1234567890", ("1988", "4", "22"), ("Maths", "English"),
                                                  ("Sports", "Music"),
                                                  "г. Санкт-Петербург, ул. Невский проспект, д 101", "NCR", "Noida")
        test_suite.tear_down()

    def test_form_positive02(self):
        test_suite.setup()
        self.automation_practice_form.fill_in_form(self.tmp_file_name, "Alexandr", "Balchugov",
                                                   "balchugov@someemail.com", "Male",
                                                   "8005553535", ("1994", "7", "20"), ("Physics", "English"),
                                                   ("Sports", "Music"),
                                                   "г. Челябинск, Кирова, 3", "NCR", "Noida")
        self.automation_practice_form.assert_result_is_displayed()
        self.automation_practice_form.assert_result_data(self.tmp_file_name, "Alexandr", "Balchugov",
                                                  "balchugov@someemail.com", "Male",
                                                  "8005553535", ("1994", "7", "20"), ("Physics", "English"),
                                                  ("Sports", "Music"),
                                                  "г. Челябинск, Кирова, 3", "NCR", "Noida")
        test_suite.tear_down()

    def tear_down(self):
        if os.path.exists(self.tmp_file_name):
            os.remove(self.tmp_file_name)
        self.automation_practice_form.tear_down()


test_suite = AutomationPracticeFormTestSuite()

try:
    test_suite.test_form_positive01()
    test_suite.test_form_positive02()
finally:
    test_suite.tear_down()
