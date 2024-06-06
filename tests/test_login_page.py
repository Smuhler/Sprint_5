from locators.register_page_locators import register_url
from locators.forgot_password_page_locators import forgot_password_url
from helpers import *
from selenium.webdriver.common.by import By


class TestLogin:

    def test_main_page_login_button_link(self, driver):
        driver.get(main_url)
        Unauthorized.click_login_button(driver)
        Unauthorized.auth_to_default_account(driver)
        assert driver.find_element(By.XPATH, main_login_button_xpath).text == 'Оформить заказ'

    def test_account_login_link(self, driver):
        driver.get(main_url)
        Unauthorized.click_account_link(driver)
        Unauthorized.auth_to_default_account(driver)
        assert driver.find_element(By.XPATH, main_login_button_xpath).text == 'Оформить заказ'

    def test_register_page_login_link(self, driver):
        driver.get(register_url)
        Unauthorized.click_footer_login_link(driver)
        Unauthorized.auth_to_default_account(driver)
        assert driver.find_element(By.XPATH, main_login_button_xpath).text == 'Оформить заказ'

    def test_forgot_password_login_link(self, driver):
        driver.get(forgot_password_url)
        Unauthorized.click_footer_login_link(driver)
        Unauthorized.auth_to_default_account(driver)
        assert driver.find_element(By.XPATH, main_login_button_xpath).text == 'Оформить заказ'
