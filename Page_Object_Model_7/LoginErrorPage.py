from selenium import webdriver # https://www.selenium.dev/documentation
from Locators import Locators

class LoginErrorPage(object):

    def __init__(self, driver):
        self.driver = driver
        self.error = driver.find_element(
            Locators.ERROR_SELECTOR[0], Locators.ERROR_SELECTOR[1]
        )
        
    def get_error_message(self):
        return self.error.text
