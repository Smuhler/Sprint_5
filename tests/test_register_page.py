from conftest import *
from locators.register_page_locators import *
from locators.login_page_locators import login_header_xpath
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions


class TestRegisterPage:

    def test_successful_register(self, create_login, create_password):
        driver = webdriver.Chrome()
        driver.get(register_url)
        driver.find_element(By.XPATH, register_name_xpath).send_keys(create_login)
        driver.find_element(By.XPATH, register_email_xpath).send_keys(create_login)
        driver.find_element(By.XPATH, register_password_xpath).send_keys(create_password)
        driver.find_element(By.XPATH, register_button_xpath).click()
        WebDriverWait(driver, 3).until(
            expected_conditions.visibility_of_element_located((By.XPATH, login_header_xpath)))
        assert '/login' in driver.current_url
        driver.quit()

    def test_incorrect_password_error(self, create_login, incorrect_password):
        driver = webdriver.Chrome()
        driver.get(register_url)
        driver.find_element(By.XPATH, register_name_xpath).send_keys(create_login)
        driver.find_element(By.XPATH, register_email_xpath).send_keys(create_login)
        driver.find_element(By.XPATH, register_password_xpath).send_keys(incorrect_password)
        driver.find_element(By.XPATH, register_button_xpath).click()
        WebDriverWait(driver, 3).until(
            expected_conditions.visibility_of_element_located((By.XPATH, './/p[text()="Некорректный пароль"]')))
        assert 'input__placeholder-filled' in driver.find_element(By.XPATH, './/label[text()="Пароль"]').get_attribute(
            'class') and driver.find_element(By.XPATH,
                                             './/label[text()="Пароль"]/parent::div/parent::div/p').text == 'Некорректный пароль'
        driver.quit()
