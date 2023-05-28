import pytest
from pages.dashboard_page import DashboardPage
from utils.config import BASE_URL

@pytest.mark.usefixtures("driver", "login")
class TestDashboard:
    def test_welcome_message(self, driver):
        dashboard_page = DashboardPage(driver)
        dashboard_page.open(BASE_URL)
        # Perform actions and assertions specific to the dashboard page
        welcome_message = dashboard_page.get_welcome_message()
        assert welcome_message == "Welcome, John Doe"

    def test_logout(self, driver):
        # Create an instance of the DashboardPage class
        dashboard_page = DashboardPage(driver)

        # Perform actions and assertions specific to the dashboard page
        dashboard_page.click_logout_button()

        # Add assertions to verify the logout behavior or navigation to the login page
