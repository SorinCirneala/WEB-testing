from pages.base_page import BasePage
from selenium.webdriver.common.by import By

# page locators
TB_URL = "https://demoqa.com/text-box"
FULLNAME_INPUT = (By.ID, "userName")
EMAIL_INPUT = (By.ID, "userEmail")

class TextboxPage(BasePage):

    # Page-specific methods
    def enter_full_name(self, fullname):
        self.enter_text(FULLNAME_INPUT, fullname)

    def enter_email(self, email):
        self.enter_text(EMAIL_INPUT, email)
