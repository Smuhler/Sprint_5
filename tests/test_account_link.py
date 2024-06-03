from constructor import *
from selenium import webdriver


class TestAccountLink:

    def test_account_link(self):
        driver = webdriver.Chrome()
        driver.get(login_url)
        Unauthorized.auth_to_default_account(driver)
        Authorized.click_account_link(driver)
        assert driver.current_url == account_profile_url
        driver.quit()
