import pytest
from time import sleep # for debugging
from pages.textbox_page import TextboxPage, TBloc

class TestTextbox:
    @pytest.mark.usefixtures("driver")
    @pytest.mark.smoke
    def test_sumbit_fullname(self, driver):
        page = TextboxPage(driver)
        page.load_page()
        page.enter_full_name("John Connor")
        page.click_submit()
        assert page.get_element_text(TBloc.NAME_LBL) == "Name:John Connor"
    
    @pytest.mark.usefixtures("driver")
    @pytest.mark.smoke
    def test_sumbit_email(self, driver):
        page = TextboxPage(driver)
        page.load_page()
        page.enter_email("sarah.connor@gmail.com")
        sleep(2)
        page.click_submit()
        sleep(2)
        assert page.get_element_text(TBloc.EMAIL_LBL) == "Email:sarah.connor@gmail.com"

    # @pytest.mark.skip(reason="in progress")