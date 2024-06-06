from helpers import *
from selenium.webdriver.common.by import By


class TestConstructor:

    def test_bun_navigation(self, driver):
        driver.get(login_url)
        Unauthorized.auth_to_default_account(driver)
        Authorized.click_sauce_span_navigation(driver)
        Authorized.click_bun_span_navigation(driver)
        assert 'tab_tab_type_current__2BEPc' in driver.find_element(By.XPATH,
                                                                    main_bun_span_selected_xpath).get_attribute('class')

    def test_sauce_navigation(self, driver):
        driver.get(login_url)
        Unauthorized.auth_to_default_account(driver)
        Authorized.click_sauce_span_navigation(driver)
        assert 'tab_tab_type_current__2BEPc' in driver.find_element(By.XPATH,
                                                                    main_sauce_span_selected_xpath).get_attribute(
            'class')

    def test_filling_navigation(self, driver):
        driver.get(login_url)
        Unauthorized.auth_to_default_account(driver)
        Authorized.click_filling_span_navigation(driver)
        assert 'tab_tab_type_current__2BEPc' in driver.find_element(By.XPATH,
                                                                    main_filling_span_selected_xpath).get_attribute(
            'class')
