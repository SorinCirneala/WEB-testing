from pages.base_page import BasePage
from selenium.webdriver.common.by import By

class TBloc():
    # page URL
    PAGE_URL = "https://demoqa.com/text-box"

    # page locators
    FULLNAME_INPUT = (By.ID, "userName")
    EMAIL_INPUT = (By.ID, "userEmail")
    CRNT_ADDRESS_INPUT = (By.ID, "currentAddress")
    PERM_ADDRESS_INPUT = (By.ID, "permanentAddress")
    SUBMIT_BTN = (By.ID, "submit")
    NAME_LBL = (By.ID, "name")
    EMAIL_LBL = (By.ID, "email")
    CRNT_ADDRESS_LBL = (By.CSS_SELECTOR, "p.mb-1") # ID is not unique
    PERM_ADDRESS_LBL = (By.ID, "permanentAddress")

class TextboxPage(BasePage):
    # override load_page method 
    def load_page(self):
        return super().load_page(TBloc.PAGE_URL)


    # Page-specific methods
    def enter_full_name(self, fullname):
        self.enter_text(TBloc.FULLNAME_INPUT, fullname)


    def enter_email(self, email):
        self.enter_text(TBloc.EMAIL_INPUT, email)


    def enter_crnt_address(self, address):
        self.enter_text(TBloc.CRNT_ADDRESS_INPUT, address)


    def enter_perm_address(self, address):
        self.enter_text(TBloc.PERM_ADDRESS_INPUT, address)


    def click_submit(self):
        self.click_element(TBloc.SUBMIT_BTN)
