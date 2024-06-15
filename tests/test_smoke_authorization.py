# Путь к драйверу для всего массива тестов
# python -m pytest -v --driver Chrome --driver-path C:/ChromeDriver_124/chromedriver-win64/chromedriver.exe tests/test_smoke_authorization.py
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


def test_authorization_valid_page_left(web_browser):
    """Проверка отображения продуктового слогана ЛК "Ростелеком ID"."""
    page = MainPage(web_browser)
    time.sleep(5)

    assert page.Page_Left.get_text() == 'Личный кабинет\nПерсональный помощник в цифровом мире Ростелекома'
    time.sleep(5)


def test_authorization_invalid_mail_cyrillic(web_browser):
    """КЭ: авторизация коректным паролем и почтой на кириллице."""
    page = MainPage(web_browser)
    time.sleep(3)

    page.Mail.click()
    page.Mail_Field.send_keys('йа.руспро@яндекс.ру')
    page.Password_Field.send_keys("12345678Qq")
    time.sleep(1)
    page.Login_Button.click()

    assert page.Invalid_Username_Or_Password.get_text() == 'Неверный логин или пароль'
    time.sleep(3)


def test_authorization_invalid_mail_bad_name(web_browser):
    """КЭ: авторизация коректным паролем и почтой с ошибкой в имени."""
    page = MainPage(web_browser)
    time.sleep(3)

    page.Mail.click()
    page.Mail_Field.send_keys('ruspro@yandex.ru')
    page.Password_Field.send_keys("12345678Qq")
    time.sleep(1)
    page.Login_Button.click()

    assert page.Invalid_Username_Or_Password.get_text() == 'Неверный логин или пароль'
    time.sleep(3)


def test_authorization_valid_mail(web_browser):
    """Авторизация корpектными почтой и паролем, переход на страницу redirect_uri."""
    page = MainPage(web_browser)
    time.sleep(5)

    page.Mail.click()
    page.Mail_Field.send_keys('ya.ruspro@yandex.ru')
    page.Password_Field.send_keys("12345678Qq")
    time.sleep(1)
    page.Login_Button.click()

    assert page.Personal_Office.get_text() == 'Личный кабинет'
    time.sleep(5)


def test_authorization_invalid_mail_bad_domain(web_browser):
    """КЭ: авторизация коректным паролем и почтой с ошибкой в домене."""
    page = MainPage(web_browser)
    time.sleep(3)

    page.Mail.click()
    page.Mail_Field.send_keys('ruspro@yandeks.ru')
    page.Password_Field.send_keys("12345678Qq")
    time.sleep(1)
    page.Login_Button.click()

    assert page.Invalid_Username_Or_Password.get_text() == 'Неверный логин или пароль'
    time.sleep(3)


def test_authorization_invalid_mail_without_doggie(web_browser):
    """КЭ: авторизация коректным паролем и почтой без символа @."""
    page = MainPage(web_browser)
    time.sleep(3)

    page.Mail.click()
    page.Mail_Field.send_keys('rusproyandeks.ru')
    page.Password_Field.send_keys("12345678Qq")
    time.sleep(1)
    page.Login_Button.click()

    assert page.Invalid_Username_Or_Password.get_text() == 'Неверный логин или пароль'
    time.sleep(3)


def test_authorization_valid_mail_caps_lock(web_browser):
    """КЭ: авторизация коректным паролем и почтой набранной при включённой клавише Caps Lock."""
    page = MainPage(web_browser)
    time.sleep(3)

    page.Mail.click()
    page.Mail_Field.send_keys('YA.RUSPRO@YANDEX.RU')
    page.Password_Field.send_keys("12345678Qq")
    time.sleep(1)
    page.Login_Button.click()

    assert page.Personal_Office.get_text() == 'Личный кабинет'
    time.sleep(3)


def test_invalid_phone_short(web_browser):
    """ГЗ: авторизация с коротким номером телефона - 10 цифр."""
    page = MainPage(web_browser)
    time.sleep(5)

    page.Phone.click()
    page.Phon_Field.send_keys('+7 960 153-57-3')
    page.Password_Field.send_keys("12345678Qq")
    time.sleep(1)

    page.Login_Button.click()

    assert page.Short_Phone_Format_Field.get_text() == 'Неверный формат телефона'
    time.sleep(3)


def test_invalid_phone_whitespace(web_browser):
    """КЭ: авторизация с пробелами вместо цифр номера телефона."""
    page = MainPage(web_browser)
    time.sleep(3)

    page.Phone.click()
    page.Phon_Field.send_keys('+         -  -  ')
    page.Password_Field.send_keys("12345678Qq")
    time.sleep(1)

    page.Login_Button.click()

    assert page.Short_Phone_Format_Field.get_text() == 'Введите номер телефона'
    time.sleep(3)


def test_authorization_valid_phone(web_browser):
    """Авторизация коректными номером телефона и паролем, переход на страницу redirect_uri."""
    page = MainPage(web_browser)
    time.sleep(3)

    page.Phone.click()
    page.Phon_Field.send_keys('+7 960 153-57-38')
    page.Password_Field.send_keys("12345678Qq")
    time.sleep(1)
    page.Login_Button.click()

    assert page.Personal_Office.get_text() == 'Личный кабинет'
    time.sleep(3)


def test_invalid_phone_latin(web_browser):
    """КЭ: авторизация с номером телефона - буквы латиница."""
    page = MainPage(web_browser)
    time.sleep(5)

    page.Phone.click()
    page.Phon_Field.send_keys('q wer tyu-io-pp')
    page.Password_Field.send_keys("12345678Qq")
    time.sleep(1)

    page.Login_Button.click()

    assert page.Invalid_Username_Or_Password.get_text() == 'Неверный логин или пароль'
    time.sleep(3)


def test_invalid_phone_cyrillic(web_browser):
    """КЭ: авторизация с номером телефона - буквы кириллица."""
    page = MainPage(web_browser)
    time.sleep(5)

    page.Phone.click()
    page.Phon_Field.send_keys('й цук енг-шщ-зз')
    page.Password_Field.send_keys("12345678Qq")
    time.sleep(1)

    page.Login_Button.click()

    assert page.Invalid_Username_Or_Password.get_text() == 'Неверный логин или пароль'
    time.sleep(3)


def test_authorization_valid_login_phone(web_browser):
    """Авторизация коректными логином (номер телефона) и паролем, переход на страницу redirect_uri."""
    page = MainPage(web_browser)
    time.sleep(5)

    page.Login.click()
    page.Login_Field.send_keys('+7 960 153-57-38')
    page.Password_Field.send_keys("12345678Qq")
    time.sleep(1)
    page.Login_Button.click()

    assert page.Personal_Office.get_text() == 'Личный кабинет'
    time.sleep(3)


def test_invalid_phone_special(web_browser):
    """КЭ: авторизация с номером телефона - спецсимволы."""
    page = MainPage(web_browser)
    time.sleep(5)

    page.Phone.click()
    page.Phon_Field.send_keys('!@#$%^&*()_')
    page.Password_Field.send_keys("12345678Qq")
    time.sleep(3)

    page.Login_Button.click()

    assert page.Invalid_Username_Or_Password.get_text() == 'Неверный логин или пароль'
    time.sleep(3)


def test_authorization_valid_login_mail(web_browser):
    """Авторизация коректными логином (e-mail) и паролем, переход на страницу redirect_uri."""
    page = MainPage(web_browser)
    time.sleep(5)

    page.Login.click()
    page.Login_Field.send_keys('ya.ruspro@yandex.ru')
    page.Password_Field.send_keys("12345678Qq")
    time.sleep(1)
    page.Login_Button.click()

    assert page.Personal_Office.get_text() == 'Личный кабинет'
    time.sleep(3)


def test_invalid_password_short(web_browser):
    """ГЗ: авторизация номером телефона и пароль 7 символов."""
    page = MainPage(web_browser)
    time.sleep(3)

    page.Phone.click()
    page.Phon_Field.send_keys('+7 960 153-57-38')
    page.Password_Field.send_keys("12347Qq")
    time.sleep(1)

    page.Login_Button.click()

    assert page.Forgot_Password.get_text() == 'Забыл пароль'
    time.sleep(3)
