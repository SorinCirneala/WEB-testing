import pytest
from time import sleep
from pages.textbox_page import TextboxPage

class TestTextbox:
    @pytest.mark.usefixtures("driver")
    @pytest.mark.smoke
    def test_sumbit_fullname(self, driver):
        driver = TextboxPage(driver)
        driver.load_page()
        driver.enter_full_name("John Connor")
        sleep(3)
    
    
    @pytest.mark.usefixtures("driver")
    @pytest.mark.regression
    def test_sumbit_email(self, driver):
        driver = TextboxPage(driver)
        driver.load_page()
        driver.enter_email("sarah.connor@gmail.com")
        sleep(3)