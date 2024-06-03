from constructor import *
from selenium import webdriver


class TestLogout:

    def test_logout_button(self):
        driver = webdriver.Chrome()
        driver.get(login_url)
        Unauthorized.auth_to_default_account(driver)
        Authorized.click_account_link(driver)
        Authorized.click_logout_button(driver)
        assert driver.current_url == login_url
        driver.quit()
