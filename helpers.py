from conftest import *
from locators.account_page_locators import *
from locators.main_page_locators import *
from locators.login_page_locators import *
from locators.register_page_locators import *
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
import random


class Register:

    @staticmethod
    def create_login():  # Генератор логина
        i = random.randint(1000, 9999)
        return f'alexeyvolkov9{i}@yandex.ru'

    @staticmethod
    def create_password():  # Генератор пароля
        return f'{random.randint(100000, 9999999)}'

    @staticmethod
    def incorrect_password():  # Генератор некорректного пароля
        return f'{random.randint(1, 99999)}'


class Unauthorized:

    @staticmethod
    def auth_to_default_account(driver):  # Авторизация статичным аккаунтом
        driver.find_element(By.XPATH, login_email_xpath).send_keys(login)
        driver.find_element(By.XPATH, login_password_xpath).send_keys(password)
        driver.find_element(By.XPATH, login_button_xpath).click()
        WebDriverWait(driver, 3).until(
            expected_conditions.visibility_of_element_located((By.XPATH, main_login_button_xpath)))

    @staticmethod
    def click_account_link(driver):  # Нажатие на кнопку "Личный кабинет"
        driver.find_element(By.XPATH, main_account_link_xpath).click()
        WebDriverWait(driver, 3).until(
            expected_conditions.visibility_of_element_located((By.XPATH, login_header_xpath)))

    @staticmethod
    def click_login_button(driver):  # Нажатие на кнопку "Войти в аккаунт"
        driver.find_element(By.XPATH, main_login_button_xpath).click()
        WebDriverWait(driver, 3).until(
            expected_conditions.visibility_of_element_located((By.XPATH, login_header_xpath)))

    @staticmethod
    def click_footer_login_link(driver):  # Нажатие на ссылку "Войти"
        driver.find_element(By.XPATH, register_login_link_xpath).click()
        WebDriverWait(driver, 3).until(
            expected_conditions.visibility_of_element_located((By.XPATH, login_header_xpath)))


class Authorized:

    @staticmethod
    def click_account_link(driver):  # Нажатие на кнопку "Личный кабинет"
        driver.find_element(By.XPATH, main_account_link_xpath).click()
        WebDriverWait(driver, 3).until(
            expected_conditions.visibility_of_element_located((By.XPATH, account_profile_link_xpath)))

    @staticmethod
    def click_constructor_link(driver):  # Нажатие на кнопку "Конструктор"
        driver.find_element(By.XPATH, main_constructor_link_xpath).click()
        WebDriverWait(driver, 3).until(
            expected_conditions.visibility_of_element_located((By.XPATH, main_login_button_xpath)))

    @staticmethod
    def click_logout_button(driver):  # Нажатие на кнопку "Выход"
        driver.find_element(By.XPATH, account_logout_button_xpath).click()
        WebDriverWait(driver, 3).until(
            expected_conditions.visibility_of_element_located((By.XPATH, login_header_xpath)))

    @staticmethod
    def click_bun_span_navigation(driver):  # Нажатие на кнопку "Булки"
        driver.find_element(By.XPATH, main_bun_span_xpath).click()
        WebDriverWait(driver, 3).until(
            expected_conditions.visibility_of_element_located((By.XPATH, main_bun_span_selected_xpath)))

    @staticmethod
    def click_sauce_span_navigation(driver):  # Нажатие на кнопку "Соусы"
        driver.find_element(By.XPATH, main_sauce_span_xpath).click()
        WebDriverWait(driver, 3).until(
            expected_conditions.visibility_of_element_located((By.XPATH, main_sauce_span_selected_xpath)))

    @staticmethod
    def click_filling_span_navigation(driver):  # Нажатие на кнопку "Начинки"
        driver.find_element(By.XPATH, main_filling_span_xpath).click()
        WebDriverWait(driver, 3).until(
            expected_conditions.visibility_of_element_located((By.XPATH, main_filling_span_selected_xpath)))
