import os

from pages.base import WebPage
from pages.elements import WebElement
from pages.elements import ManyWebElements


class MainPage(WebPage):

    def __init__(self, web_driver, url=''):
        if not url:
            url = os.getenv("MAIN_URL") or 'https://b2c.passport.rt.ru/auth'

        super().__init__(web_driver, url)

# Страница автризации
    # Баннер Авторизация
    Banner_Athorization = WebElement(id='card-title')
    # Поле Неверный логин или пароль
    Invalid_Username_Or_Password = WebElement(id='form-error-message')
    # Кнопка Зарегистрироваться авторизация
    Register = WebElement(id='kc-register')
    # Кнопка Зарегистрироваться регистрация
    Register_Register = WebElement(name='register')
    # Кнопка телефон
    Phone = WebElement(id='t-btn-tab-phone')
    # Кнопка почта
    Mail = WebElement(id='t-btn-tab-mail')
    # Кнопка логин
    Login = WebElement(id='t-btn-tab-login')
    # Кнопка Лицевой счёт
    Personal_Account = WebElement(id='t-btn-tab-ls')
    # Поле телефон
    Phon_Field = WebElement(id='username')
    # Поле Неверный формат телефона
    Short_Phone_Format_Field = WebElement(id='username-meta')
    # Поле почта
    Mail_Field = WebElement(id='username')
    # Поле логин
    Login_Field = WebElement(id='username')
    # Поле Лицевой счёт
    Personal_Account_Field = WebElement(id='username')
    # Поле пароль
    Password_Field = WebElement(id='password')
    # Кнопка войти
    Login_Button = WebElement(id='kc-login')
    # Кнопка Пользовательское соглашение
    User_Agreement = WebElement(id='rt-auth-agreement-link')

# Страница регистрации

    # Поле Имя
    First_Name = WebElement(name='firstName')
    # Поле Фамилия
    Last_Name = WebElement(name='lastName')
    # Поле Регион Город
    City = WebElement(css_selector='rt-input__input rt-select__input rt-input__input--rounded rt-input__input--orange')
    # Поле E-mail или телефон
    Mail_Or_Phone = WebElement(id='address')
    # Поле Подтверждение пароля
    Password_confirm = WebElement(id='password-confirm')
    # Поле Регистрация финал
    Register_Final = WebElement(css_selector='rt-btn rt-btn--orange rt-btn--medium rt-btn--rounded register-form__reg-btn')
    # Поле Личный кабинет
    Personal_Office = WebElement(id='id_app_lk_b2c')
    # Кнопка забыл пароль
    Forgot_Password = WebElement(id='forgot_password')
    # Продуктовый слоган ЛК "Ростелеком ID".
    Page_Left = WebElement(id='page-left')
    # предупреждение ошибки имени
    Error_First_Name = WebElement(css_selector="#page-right > div > div.card-container__wrapper > div > form > "
                                               "div.name-container > div.rt-input-container.rt-input-container--error"
                                               " > span")
    # Предупреждение ошибки пароля
    Error_Password = WebElement(css_selector="#page-right > div > div.card-container__wrapper > div > form > "
                                             "div.new-password-container > "
                                             "div.rt-input-container.rt-input-container--error.new-password-container__password > span")
    # Поле предупреждения - подтверждение пароля не совпадает с паролем
    Mismatch_Password = WebElement(css_selector="#page-right > div > div.card-container__wrapper > div > form > "
                                                "div.new-password-container > "
                                                "div.rt-input-container.rt-input-container--error.new-password-container__confirmed-password > span")