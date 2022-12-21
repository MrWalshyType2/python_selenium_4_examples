from selenium import webdriver # https://www.selenium.dev/documentation
from Locators import Locators

class LoginPage(object):

    def __init__(self, driver):
        self.driver = driver
        self.username_input = driver.find_element(
            Locators.USERNAME_SELECTOR[0], Locators.USERNAME_SELECTOR[1]
        )
        self.password_input = driver.find_element(
            Locators.PASSWORD_SELECTOR[0], Locators.PASSWORD_SELECTOR[1]
        )
        self.login_btn = driver.find_element(
            Locators.LOGIN_BTN_SELECTOR[0], Locators.LOGIN_BTN_SELECTOR[1]
        )
        
    def login(self, username, password):
        self.username_input.send_keys(username)
        self.password_input.send_keys(password)
        self.login_btn.click()
