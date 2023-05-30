from pages.base_page import BasePage
from selenium.webdriver.common.by import By


# page URL
TEXTBOX_PAGE_URL = "https://demoqa.com/text-box"

# page locators
FULLNAME_INPUT = (By.ID, "userName")
EMAIL_INPUT = (By.ID, "userEmail")

class TextboxPage(BasePage):
    # override load_page method 
    def load_page(self):
        return super().load_page(TEXTBOX_PAGE_URL)

    # Page-specific methods
    def enter_full_name(self, fullname):
        self.enter_text(FULLNAME_INPUT, fullname)

    def enter_email(self, email):
        self.enter_text(EMAIL_INPUT, email)
