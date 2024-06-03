import random
import pytest

# Статичный аккаунт для авторизованной зоны
login = 'alexeyvolkov9constant@yandex.ru'
password = 'vsem privet'


@pytest.fixture
def create_login():  # Генератор логина
    i = random.randint(1000, 9999)
    return f'alexeyvolkov9{i}@yandex.ru'


@pytest.fixture
def create_password():  # Генератор пароля
    return f'{random.randint(100000, 9999999)}'


@pytest.fixture
def incorrect_password():  # Генератор некорректного пароля
    return f'{random.randint(1, 99999)}'
