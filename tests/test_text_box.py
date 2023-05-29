

import pytest
from time import sleep
from pages.textbox_page import TextboxPage, TEXTBOX_URL
# from utils.config import BASE_URL

@pytest.mark.usefixtures("driver", "login")
class TestTextbox:
    def test_sumbit_fullname(self, driver):
        page = TextboxPage(driver)
        page.open(TEXTBOX_URL)
        page.enter_full_name("John Connor")
        sleep(3)


    # def test_logout(self, driver):
    #     # Create an instance of the DashboardPage class
    #     text_box_page = DashboardPage(driver)

    #     # Perform actions and assertions specific to the dashboard page
    #     text_box_page.click_logout_button()

    #     # Add assertions to verify the logout behavior or navigation to the login page
