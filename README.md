# Rostelecom-PJ-04
Введение
Этот репозиторий содержит пример использования ранее предложеного коамандой курса шаблона PageObject с Selenium и Python (PyTest + Selenium).

Файлы
conftest.py содержит весь необходимый код для отслеживания неудачных тестовых примеров и создания скриншота страницы на случай, если какой-либо тестовый пример завершится неудачей.

pages/base.py содержит реализацию шаблона PageObject для Python.

pages/elements.py содержит вспомогательный класс для определения веб-элементов на веб-страницах.

тесты /test_smoke_authorization.py и test_smoke_registration.py содержит несколько тестов smoke Web UI для Ростелекома (https://b2c.passport.rt.ru/auth)

Как запускать тесты
Установите все требования:

требования к установке pip3 -r.
Скачайте Selenium WebDriver с https://chromedriver.chromium.org/downloads (выберите версию, совместимую с вашим браузером)

Запуск тестов:

python3 -m pytest -v --driver Chrome --путь к драйверу ~/chrome tests/*
alt text

Примечание: ~/chrome в этом примере представляет собой файл Selenium WebDriver.
