from pages.base_page import BasePage
from selenium.webdriver.common.by import By

class TextboxPage(BasePage):
    # Define locators specific to the dashboard page
    TEXTBOX_URL = 'https://demoqa.com/text-box'
    FULL_NAME_INPUT = (By.ID, 'userName')
    EMAIL_INPUT = (By.ID, 'userEmail')

    # Define page-specific methods
    def enter_full_name(self, fullname):
        self.enter_text(self.FULL_NAME_INPUT, fullname)

    def enter_email(self, email):
        self.enter_text(self.EMAIL_INPUT, email)
