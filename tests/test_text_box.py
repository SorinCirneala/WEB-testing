import sys, os
project_path = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, project_path)

import pytest
from time import sleep
from pages.textbox_page import TextboxPage, TB_URL

@pytest.mark.usefixtures("driver", "login")
@pytest.mark.smoke
class TestTextbox:
    def test_sumbit_fullname(self, driver):
        page = TextboxPage(driver)
        page.open(TB_URL)
        page.enter_full_name("John Connor")
        page.enter_email
        sleep(3)


    # def test_logout(self, driver):
    #     # Create an instance of the DashboardPage class
    #     text_box_page = DashboardPage(driver)

    #     # Perform actions and assertions specific to the dashboard page
    #     text_box_page.click_logout_button()

    #     # Add assertions to verify the logout behavior or navigation to the login page
