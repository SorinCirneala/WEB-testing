import pytest
from selenium import webdriver
from selenium.webdriver import ChromeOptions

@pytest.fixture(scope="session")
def driver():
    # to remove DevTools listening on... warning
    options = ChromeOptions() 
    options.add_experimental_option('excludeSwitches', ['enable-logging']) 

    # set up code: create and configure driver
    driver = webdriver.Chrome(options=options)
    driver.maximize_window()

    # pass driver to test case
    yield driver
    
    # teardown code: quit the driver and clean up any resources
    driver.quit()


@pytest.fixture(scope="function")
def login(driver):
    # setup code
    yield
    # teardown code
