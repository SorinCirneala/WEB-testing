import pytest
from pages.text_box_page import TextboxPage, TEXTBOX_URL
# from utils.config import BASE_URL

@pytest.mark.usefixtures("driver", "login")
class TestDashboard:
    def test_welcome_message(self, driver):
        text_box_page = TextboxPage(driver)
        text_box_page.open(TEXTBOX_URL)
        # Perform actions and assertions specific to the dashboard page
        welcome_message = text_box_page.get_welcome_message()
        assert welcome_message == "Welcome, John Doe"

    def test_logout(self, driver):
        # Create an instance of the DashboardPage class
        text_box_page = DashboardPage(driver)

        # Perform actions and assertions specific to the dashboard page
        text_box_page.click_logout_button()

        # Add assertions to verify the logout behavior or navigation to the login page
