import pytest
from selenium import webdriver

# Статичный аккаунт для авторизованной зоны
login = 'alexeyvolkov9constant@yandex.ru'
password = 'vsem privet'


@pytest.fixture(scope="function")
def driver():
    options = webdriver.ChromeOptions()
    options.add_argument('--ignore-certificate-errors')
    options.add_argument('--ignore-ssl-errors')
    chrome_driver = webdriver.Chrome(options=options)
    yield chrome_driver
    chrome_driver.close()
