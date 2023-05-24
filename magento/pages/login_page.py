from locators import EMAIL_FIELD, PASS_FIELD, SIGNIN_BTN, PAGE_TITLE_LBL, ERROR_MSG
from pages.base_page import BasePage

class LoginPage(BasePage):
    # open the page, initializes the required variables
    def __init__(self):
        super().__init__()
        self.driver.maximize_window()
        self.driver.get("https://magento.softwaretestingboard.com/customer/account/login/")

    # page actions
    def enter_email(self, email):
        self.set_text(EMAIL_FIELD, email)

    def enter_pass(self, password):
        self.set_text(PASS_FIELD, password)

    def click_sign_in(self):
        self.click_element(SIGNIN_BTN)

    def get_page_title(self):
        return self.get_text(PAGE_TITLE_LBL)

    def get_error_msg(self):
        return self.get_text(ERROR_MSG)

    # def login(self, username=None, password=None):
    #     """ Enter user, password, click login button """
    #     username = username if username else self.user_name
    #     password = password if password else self.passwrd

    #     self.set_text(self.get_element(locators.USERNAME_INPUT), username)
    #     self.set_text(self.get_element(locators.PASSWORD_INPUT), password)
    #     self.click_element(self.get_element(locators.LOGIN_BUTTON))