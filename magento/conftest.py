import pytest
from selenium import webdriver

@pytest.fixture(scope="session")
def driver():
    driver = webdriver.Chrome()
    
    # Set up any additional configuration for the driver
    
    yield driver
    
    # Teardown - quit the driver and clean up any resources
    driver.quit()

@pytest.fixture(scope="function")
def login(driver):
    # Perform login actions, such as navigating to the login page,
    # entering credentials, and submitting the form.
    
    # Optionally, you can return any data or objects needed for the tests
    
    yield
    
    # Teardown - perform any necessary cleanup after the test
    # For example, log out or navigate to a different page.
