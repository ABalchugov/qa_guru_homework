
import time
from selenium import webdriver
from selenium.webdriver.common.by import By

def set_up(driver):
    driver.get("https://qa-guru.github.io/one-page-form/text-box.html")
    driver.maximize_window()
    time.sleep(5)

def tear_down(driver):
    driver.quit()

#Тест поля FullName
def test_full_name():
    # Запуск браузера Chrome
    driver = webdriver.Chrome()

    try:
        # Открытие страницы
        set_up(driver)

        # Поиск элементов и заполнение полей
        full_name_field = driver.find_element(By.ID, "userName")
        full_name_field.send_keys("Александр Александров")

        # Находим поле Email по его ID и вводим текст
        email_field = driver.find_element(By.ID, "userEmail")
        email_field.send_keys("alexandr@example.com")

        # Находим кнопку Submit по ее ID и кликаем
        submit_button = driver.find_element(By.ID, "submit")
        submit_button.click()

        # Проверка результата
        time.sleep(5)  # Пауза, чтобы увидеть результат отправки

        # Находим блок с отправленными данными
        result_box = driver.find_element(By.ID, "output")

        # Проверяем, что в блоке результата появился введенный текст
        assert "Александр Александров" in result_box.text
        print("Тест поля Full Name успешно пройден!")

    finally:
        # Закрытие браузера в любом случае
        tear_down(driver)

#Негативный тест поля Email без @
def test_email_negative():
    # Запуск браузера Chrome
    driver = webdriver.Chrome()

    try:
        # Открытие страницы
        set_up(driver)

        # Поиск элементов и заполнение полей
        # Находим поле Full Name по его ID и вводим текст
        full_name_field = driver.find_element(By.ID, "userName")
        full_name_field.send_keys("Александр Александров")

        # Находим поле Email по его ID и вводим текст
        email_field = driver.find_element(By.ID, "userEmail")
        email_field.send_keys("alexandrexample.com")

        # Находим кнопку Submit по ее ID и кликаем
        submit_button = driver.find_element(By.ID, "submit")
        submit_button.click()

        # Проверка результата
        time.sleep(5)  # Пауза, чтобы увидеть результат отправки

        # Находим блок с отправленными данными
        result_box = driver.find_element(By.ID, "output")

        # Проверяем, что в блоке результата появился введенный текст
        assert "alexandrexample.com" not in result_box.text
        print("Негативный тест поля Email успешно пройден!")

    finally:
        # Закрытие браузера в любом случае
        tear_down(driver)

#Тест поля Current Address
def test_current_address():
    # Запуск браузера Chrome
    driver = webdriver.Chrome()

    try:
        # Открытие страницы
        set_up(driver)

        # Поиск элементов и заполнение полей
        # Находим поле Full Name по его ID и вводим текст
        full_name_field = driver.find_element(By.ID, "userName")
        full_name_field.send_keys("Александр Александров")

        # Находим поле Email по его ID и вводим текст
        email_field = driver.find_element(By.ID, "userEmail")
        email_field.send_keys("alexandr@example.com")

        # Находим поле Current Address по его ID и вводим текст
        current_address_field = driver.find_element(By.ID, "currentAddress")
        current_address_field.send_keys("Москва, Петровка, 38")

        # Находим кнопку Submit по ее ID и кликаем
        submit_button = driver.find_element(By.ID, "submit")
        submit_button.click()

        # Проверка результата
        time.sleep(5)  # Пауза, чтобы увидеть результат отправки

        # Находим блок с отправленными данными
        result_box = driver.find_element(By.ID, "output")

        # Проверяем, что в блоке результата появился введенный текст
        assert "Москва, Петровка, 38" in result_box.text
        print("Тест поля Current Address успешно пройден!")

    finally:
        # Закрытие браузера в любом случае
        tear_down(driver)

#Тест поля Permanent Address
def test_permanent_address():
    # Запуск браузера Chrome
    driver = webdriver.Chrome()

    try:
        # Открытие страницы
        set_up(driver)

        # Поиск элементов и заполнение полей
        # Находим поле Full Name по его ID и вводим текст
        full_name_field = driver.find_element(By.ID, "userName")
        full_name_field.send_keys("Александр Александров")

        # Находим поле Email по его ID и вводим текст
        email_field = driver.find_element(By.ID, "userEmail")
        email_field.send_keys("alexandr@example.com")

        # Находим поле Permanent Address по его ID и вводим текст
        permanent_address_field = driver.find_element(By.ID, "permanentAddress")
        permanent_address_field.send_keys("Москва, Б. Лубянка, 2")

        # Находим кнопку Submit по ее ID и кликаем
        submit_button = driver.find_element(By.ID, "submit")
        submit_button.click()

        # Проверка результата
        time.sleep(5)  # Пауза, чтобы увидеть результат отправки

        # Находим блок с отправленными данными
        result_box = driver.find_element(By.ID, "output")

        # Проверяем, что в блоке результата появился введенный текст
        assert "Москва, Б. Лубянка, 2" in result_box.text
        print("Тест поля Permanent Address успешно пройден!")

    finally:
        # Закрытие браузера в любом случае
        tear_down(driver)

test_full_name()
test_email_negative()
test_current_address()
test_permanent_address()