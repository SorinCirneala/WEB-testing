from selenium import webdriver
from selenium.webdriver import ChromeOptions
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.remote.webelement import WebElement


class BasePage:
    def __init__(self):
        service = Service(executable_path="../tools/chromedriver.exe") # to remove DeprecationWarning
        options = ChromeOptions() # to remove DevTools listening on... warning
        options.add_experimental_option('excludeSwitches', ['enable-logging']) 
        self.driver = webdriver.Chrome(service=service, options=options)
        self.wait = WebDriverWait(self.driver, 10)

    def get_element(self, locator) -> WebElement:
        return self.wait.until(EC.presence_of_element_located(locator))

    def get_all_elements(self, locator) -> list:
        element_list = self.driver.find_elements(*locator)
        return element_list

    def click_element(self, locator):
        element = self.get_element(locator)
        element.click()

    def set_text(self, locator, text):
        element = self.get_element(locator)
        element.clear()
        element.send_keys(text)

    def get_text(self, locator) -> str:
        element = self.get_element(locator)
        return element.text
