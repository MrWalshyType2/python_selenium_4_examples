from selenium import webdriver # https://www.selenium.dev/documentation
from Locators import Locators

class LoginLandingPage(object):

    def __init__(self, driver):
        self.driver = driver
        self.products = driver.find_elements(
            Locators.INVENTORY_ITEM_SELECTOR[0], Locators.INVENTORY_ITEM_SELECTOR[1]
        )
        
    def did_products_load(self):
        return len(self.products) > 0
