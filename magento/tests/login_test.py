import sys, os
project_path = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, project_path)

from time import sleep

from credentials import email, password
from pages.login_page import LoginPage


def test_login_correct_credentials():
    page = LoginPage()
    page.enter_email(email)
    page.enter_pass(password)
    page.click_sign_in()
    sleep(2)
    page_title = page.get_page_title() 
    assert page_title == "My Account"

def test_login_wrong_credentials():
    page = LoginPage()
    page.enter_email("wrong.email@wrong.com")
    page.enter_pass("wrong")
    page.click_sign_in()
    sleep(2)
    error_msg = page.get_error_msg()
    print(error_msg)
    assert error_msg == "The account sign-in was incorrect or your account is disabled temporarily. Please wait and try again later."
