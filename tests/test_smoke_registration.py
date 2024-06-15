# Путь к драйверу для всего массива тестов
# python -m pytest -v --driver Chrome --driver-path C:/ChromeDriver_124/chromedriver-win64/chromedriver.exe tests/test_smoke_registration.py
# Путь к драйверу для конкретного теста
# python -m pytest -v --driver Chrome --driver-path C:\Chrome-selenium\chromedriver.exetests\test.py -k test_button_phone
# python -m pytest -v --driver Chrome --driver-path C:\Chrome-selenium\chromedriver.exetests\test.py -k test_button_mail
# python -m pytest -v --driver Chrome --driver-path C:\Chrome-selenium\chromedriver.exetests\test.py -k test_authorisation

# КЭ - Kлассы эквивалентности
# ГЗ - Граничные значения


from pages.rostelecom import MainPage

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

import time
import pytest
from selenium import webdriver
import chromedriver_autoinstaller

chromedriver_autoinstaller.install()


@pytest.fixture(autouse=True)
def driver():
    driver = webdriver.Chrome()
    driver.maximize_window()
    yield driver
    driver.quit()


def test_auth(driver):
    """Зайти на страничку Ростелеком в неавторизованном режиме."""
    time.sleep(3)
    driver.get('https://b2c.passport.rt.ru/auth')
    time.sleep(5)


def test_invalid_registration_short_name(web_browser):
    """ГЗ: pегистрация с именем из одной буквы кириллицы."""
    page = MainPage(web_browser)
    time.sleep(3)

    page.Register.click()
    page.First_Name.click()
    page.First_Name.send_keys("Ю")
    page.Last_Name.click()
    page.Last_Name.send_keys("Юююю")
    # page.City.click()
    page.Mail_Or_Phone.click()
    page.Mail_Or_Phone.send_keys('+7 960 153-57-38')
    page.Password_Field.click()
    page.Password_Field.send_keys('12345678Ww')
    page.Password_confirm.click()
    page.Password_confirm.send_keys('12345678Ww')
    page.Register_Register.click()

    assert page.Error_First_Name.get_text() == 'Необходимо заполнить поле кириллицей. От 2 до 30 символов.'
    time.sleep(3)


def test_invalid_registration_long_name(web_browser):
    """ГЗ: pегистрация с именем из тридцати одной буквы кириллицы."""
    page = MainPage(web_browser)
    time.sleep(3)

    page.Register.click()
    page.First_Name.click()
    page.First_Name.send_keys("Ююююююююююююююююююююююююююююююю")
    page.Last_Name.click()
    page.Last_Name.send_keys("Юююю")
    # page.City.click()
    page.Mail_Or_Phone.click()
    page.Mail_Or_Phone.send_keys('+7 960 153-57-38')
    page.Password_Field.click()
    page.Password_Field.send_keys('12345678Ww')
    page.Password_confirm.click()
    page.Password_confirm.send_keys('12345678Ww')
    page.Register_Register.click()

    assert page.Error_First_Name.get_text() == 'Необходимо заполнить поле кириллицей. От 2 до 30 символов.'
    time.sleep(3)


def test_invalid_registration_latin_name(web_browser):
    """КЭ: pегистрация с именем на латинице."""
    page = MainPage(web_browser)
    time.sleep(3)

    page.Register.click()
    page.First_Name.click()
    page.First_Name.send_keys("Uuu")
    page.Last_Name.click()
    page.Last_Name.send_keys("Юююю")
    # page.City.click()
    page.Mail_Or_Phone.click()
    page.Mail_Or_Phone.send_keys('+7 960 153-57-38')
    page.Password_Field.click()
    page.Password_Field.send_keys('12345678Ww')
    page.Password_confirm.click()
    page.Password_confirm.send_keys('12345678Ww')
    page.Register_Register.click()

    assert page.Error_First_Name.get_text() == 'Необходимо заполнить поле кириллицей. От 2 до 30 символов.'
    time.sleep(3)


def test_invalid_registration_special_name(web_browser):
    """КЭ: pегистрация с именем c использованием спецсимволов."""
    page = MainPage(web_browser)
    time.sleep(3)

    page.Register.click()
    page.First_Name.click()
    page.First_Name.send_keys('@#$%^')
    page.Last_Name.click()
    page.Last_Name.send_keys("Юююю")
    # page.City.click()
    page.Mail_Or_Phone.click()
    page.Mail_Or_Phone.send_keys('+7 960 153-57-38')
    page.Password_Field.click()
    page.Password_Field.send_keys('12345678Ww')
    page.Password_confirm.click()
    page.Password_confirm.send_keys('12345678Ww')
    page.Register_Register.click()

    assert page.Error_First_Name.get_text() == 'Необходимо заполнить поле кириллицей. От 2 до 30 символов.'
    time.sleep(3)


def test_invalid_registration_empty_name(web_browser):
    """КЭ: pегистрация с пустой строкой вместо имени."""
    page = MainPage(web_browser)
    time.sleep(3)

    page.Register.click()
    page.First_Name.click()
    page.First_Name.send_keys(' ')
    page.Last_Name.click()
    page.Last_Name.send_keys("Юююю")
    # page.City.click()
    page.Mail_Or_Phone.click()
    page.Mail_Or_Phone.send_keys('+7 960 153-57-38')
    page.Password_Field.click()
    page.Password_Field.send_keys('12345678Ww')
    page.Password_confirm.click()
    page.Password_confirm.send_keys('12345678Ww')
    page.Register_Register.click()

    assert page.Error_First_Name.get_text() == 'Необходимо заполнить поле кириллицей. От 2 до 30 символов.'
    time.sleep(3)


def test_invalid_registration_digit_name(web_browser):
    """КЭ: pегистрация с именем c использованием чисел."""
    page = MainPage(web_browser)
    time.sleep(3)

    page.Register.click()
    page.First_Name.click()
    page.First_Name.send_keys('1234')
    page.Last_Name.click()
    page.Last_Name.send_keys("Юююю")
    # page.City.click()
    page.Mail_Or_Phone.click()
    page.Mail_Or_Phone.send_keys('+7 960 153-57-38')
    page.Password_Field.click()
    page.Password_Field.send_keys('12345678Ww')
    page.Password_confirm.click()
    page.Password_confirm.send_keys('12345678Ww')
    page.Register_Register.click()

    assert page.Error_First_Name.get_text() == 'Необходимо заполнить поле кириллицей. От 2 до 30 символов.'
    time.sleep(3)


def test_invalid_registration_short_password(web_browser):
    """ГЗ: количество символов пароля 7."""
    page = MainPage(web_browser)
    time.sleep(3)

    page.Register.click()
    page.First_Name.click()
    page.First_Name.send_keys('Ююю')
    page.Last_Name.click()
    page.Last_Name.send_keys("Юююю")
    # page.City.click()
    page.Mail_Or_Phone.click()
    page.Mail_Or_Phone.send_keys('+7 960 153-57-38')
    page.Password_Field.click()
    page.Password_Field.send_keys('12345Ww')
    page.Password_confirm.click()
    page.Password_confirm.send_keys('12345Ww')
    page.Register_Register.click()

    assert page.Error_Password.get_text() == 'Длина пароля должна быть не менее 8 символов'
    time.sleep(3)


def test_invalid_registration_empty_password(web_browser):
    """КЭ: pегистрация с пробелом вместо пароля."""
    page = MainPage(web_browser)
    time.sleep(3)

    page.Register.click()
    page.First_Name.click()
    page.First_Name.send_keys('Ююю')
    page.Last_Name.click()
    page.Last_Name.send_keys("Юююю")
    # page.City.click()
    page.Mail_Or_Phone.click()
    page.Mail_Or_Phone.send_keys('+7 960 153-57-38')
    page.Password_Field.click()
    page.Password_Field.send_keys(' ')
    page.Password_confirm.click()
    page.Password_confirm.send_keys(' ')
    page.Register_Register.click()

    assert page.Error_Password.get_text() == 'Длина пароля должна быть не менее 8 символов'
    time.sleep(3)


def test_invalid_registration_no_capital_letter_password(web_browser):
    """КЭ: в пароле нет заглавной буквы."""
    page = MainPage(web_browser)
    time.sleep(3)

    page.Register.click()
    page.First_Name.click()
    page.First_Name.send_keys('Ююю')
    page.Last_Name.click()
    page.Last_Name.send_keys("Юююю")
    # page.City.click()
    page.Mail_Or_Phone.click()
    page.Mail_Or_Phone.send_keys('+7 960 153-57-38')
    page.Password_Field.click()
    page.Password_Field.send_keys('12345678ww')
    page.Password_confirm.click()
    page.Password_confirm.send_keys('12345678ww')
    page.Register_Register.click()

    assert page.Error_Password.get_text() == 'Пароль должен содержать хотя бы одну заглавную букву'
    time.sleep(3)


def test_invalid_registration_no_lowercase_letter_password(web_browser):
    """КЭ: в пароле нет cтрочной буквы."""
    page = MainPage(web_browser)
    time.sleep(3)

    page.Register.click()
    page.First_Name.click()
    page.First_Name.send_keys('Ююю')
    page.Last_Name.click()
    page.Last_Name.send_keys("Юююю")
    # page.City.click()
    page.Mail_Or_Phone.click()
    page.Mail_Or_Phone.send_keys('+7 960 153-57-38')
    page.Password_Field.click()
    page.Password_Field.send_keys('12345678WW')
    page.Password_confirm.click()
    page.Password_confirm.send_keys('12345678WW')
    page.Register_Register.click()

    assert page.Error_Password.get_text() == 'Пароль должен содержать хотя бы одну строчную букву'
    time.sleep(3)


def test_invalid_registration_cyrillic_password(web_browser):
    """КЭ: в пароле есть буквы на кириллице."""
    page = MainPage(web_browser)
    time.sleep(3)

    page.Register.click()
    page.First_Name.click()
    page.First_Name.send_keys('Ююю')
    page.Last_Name.click()
    page.Last_Name.send_keys("Юююю")
    # page.City.click()
    page.Mail_Or_Phone.click()
    page.Mail_Or_Phone.send_keys('+7 960 153-57-38')
    page.Password_Field.click()
    page.Password_Field.send_keys('12345678Цц')
    page.Password_confirm.click()
    page.Password_confirm.send_keys('12345678Цц')
    page.Register_Register.click()

    assert page.Error_Password.get_text() == 'Пароль должен содержать только латинские буквы'
    time.sleep(3)

def test_invalid_registration_mismatch_password(web_browser):
    """Попарное тестирование: в поле "Подтверждение пароля" пароль отличный от пароля в поле "Пароль."""
    page = MainPage(web_browser)
    time.sleep(3)

    page.Register.click()
    page.First_Name.click()
    page.First_Name.send_keys('Ююю')
    page.Last_Name.click()
    page.Last_Name.send_keys("Юююю")
    # page.City.click()
    page.Mail_Or_Phone.click()
    page.Mail_Or_Phone.send_keys('+7 960 153-57-38')
    page.Password_Field.click()
    page.Password_Field.send_keys('12345678Ww')
    page.Password_confirm.click()
    page.Password_confirm.send_keys('12345678Ee')
    page.Register_Register.click()

    assert page.Mismatch_Password.get_text() == 'Пароли не совпадают'
    time.sleep(3)