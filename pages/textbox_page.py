from pages.base_page import BasePage
from selenium.webdriver.common.by import By


# page URL
TEXTBOX_PAGE_URL = "https://demoqa.com/text-box"

# page locators
FULLNAME_INPUT = (By.ID, "userName")
EMAIL_INPUT = (By.ID, "userEmail")
CRNT_ADDRESS_INPUT = (By.ID, "currentAddress")
PERM_ADDRESS_INPUT = (By.ID, "permanentAddress")
SUBMIT_BTN = (By.ID, "submit")
NAME_LBL = (By.ID, "name")
EMAIL_LBL = (By.ID, "email")
CRNT_ADDRESS_LBL = (By.ID, "currentAddress")
PERM_ADDRESS_LBL = (By.ID, "permanentAddress")

class TextboxPage(BasePage):
    # override load_page method 
    def load_page(self):
        return super().load_page(TEXTBOX_PAGE_URL)


    # Page-specific methods
    def enter_full_name(self, fullname):
        self.enter_text(FULLNAME_INPUT, fullname)


    def enter_email(self, email):
        self.enter_text(EMAIL_INPUT, email)


    def enter_crnt_address(self, address):
        self.enter_text(CRNT_ADDRESS_INPUT, address)


    def enter_perm_address(self, address):
        self.enter_text(PERM_ADDRESS_INPUT, address)


    def click_submit(self):
        self.click_element(SUBMIT_BTN)


    def get_name_output(self):
        name_elem = self.find_element(NAME_LBL)
        return name_elem.text


    def get_email_output(self):
        email_elem = self.find_element(NAME_LBL)
        return email_elem.text