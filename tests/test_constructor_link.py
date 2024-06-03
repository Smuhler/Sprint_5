from constructor import *
from selenium import webdriver
from selenium.webdriver.common.by import By


class TestConstructorLink:

    def test_constructor_link(self):
        driver = webdriver.Chrome()
        driver.get(login_url)
        Unauthorized.auth_to_default_account(driver)
        Authorized.click_account_link(driver)
        Authorized.click_constructor_link(driver)
        assert driver.find_element(By.XPATH, main_login_button_xpath).text == 'Оформить заказ'
        driver.quit()
