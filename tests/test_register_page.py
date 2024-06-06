from conftest import *
from helpers import Register
from locators.register_page_locators import *
from locators.login_page_locators import login_header_xpath
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions


class TestRegisterPage:

    def test_successful_register(self, driver):
        driver.get(register_url)
        driver.find_element(By.XPATH, register_name_input_xpath).send_keys(Register.create_login())
        driver.find_element(By.XPATH, register_email_input_xpath).send_keys(Register.create_login())
        driver.find_element(By.XPATH, register_password_input_xpath).send_keys(Register.create_password())
        driver.find_element(By.XPATH, register_button_xpath).click()
        WebDriverWait(driver, 3).until(
            expected_conditions.visibility_of_element_located((By.XPATH, login_header_xpath)))
        assert '/login' in driver.current_url

    def test_incorrect_password_error(self, driver):
        driver.get(register_url)
        driver.find_element(By.XPATH, register_name_input_xpath).send_keys(Register.create_login())
        driver.find_element(By.XPATH, register_email_input_xpath).send_keys(Register.create_login())
        driver.find_element(By.XPATH, register_password_input_xpath).send_keys(Register.incorrect_password())
        driver.find_element(By.XPATH, register_button_xpath).click()
        WebDriverWait(driver, 3).until(
            expected_conditions.visibility_of_element_located((By.XPATH, register_incorrect_password_text_xpath)))
        assert 'input_status_error' in driver.find_element(By.XPATH, register_password_div_xpath).get_attribute(
            'class')
