from pages.base_page import BasePage
from selenium.webdriver.common.by import By

class DashboardPage(BasePage):
    # Define locators specific to the dashboard page
    WELCOME_MESSAGE = (By.CSS_SELECTOR, '#welcome-message')
    LOGOUT_BUTTON = (By.ID, 'logout-button')

    # Define page-specific methods
    def get_welcome_message(self):
        return self.find_element(self.WELCOME_MESSAGE).text

    def click_logout_button(self):
        self.click_element(self.LOGOUT_BUTTON)
