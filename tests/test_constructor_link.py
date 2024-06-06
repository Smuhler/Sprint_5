from helpers import *
from selenium.webdriver.common.by import By


class TestConstructorLink:

    def test_constructor_link(self, driver):
        driver.get(login_url)
        Unauthorized.auth_to_default_account(driver)
        Authorized.click_account_link(driver)
        Authorized.click_constructor_link(driver)
        assert driver.find_element(By.XPATH, main_login_button_xpath).text == 'Оформить заказ'
