import pytest
from time import sleep # for debugging
from pages.textbox_page import TextboxPage, TBloc
from utils.parametrize import get_input

class TestTextbox:
    @pytest.mark.parametrize("name", get_input("test_sumbit_fullname"))
    @pytest.mark.usefixtures("driver")
    @pytest.mark.smoke
    def test_sumbit_fullname(self, driver, name):
        page = TextboxPage(driver)
        page.load_page()
        page.enter_full_name(name)
        page.click_submit()
        assert page.get_element_text(TBloc.NAME_LBL) == f"Name:{name}"
    
    @pytest.mark.usefixtures("driver")
    @pytest.mark.smoke
    def test_sumbit_email(self, driver):
        page = TextboxPage(driver)
        page.load_page()
        page.enter_email("sarah.connor@gmail.com")
        page.click_submit()
        assert page.get_element_text(TBloc.EMAIL_LBL) == "Email:sarah.connor@gmail.com"

    # @pytest.mark.skip(reason="in progress")
    @pytest.mark.usefixtures("driver")
    @pytest.mark.smoke
    def test_sumbit_current_address(self, driver):
        page = TextboxPage(driver)
        page.load_page()
        page.enter_crnt_address("4660, Great American Parkway, Santa Clara, CA")
        page.click_submit()
        assert page.get_element_text(TBloc.CRNT_ADDRESS_LBL) == "Current Address :4660, Great American Parkway, Santa Clara, CA"
