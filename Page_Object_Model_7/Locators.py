from selenium import webdriver # https://www.selenium.dev/documentation
from selenium.webdriver.common.by import By

class Locators(object):
    USERNAME_SELECTOR = (By.NAME, "user-name")
    PASSWORD_SELECTOR = (By.NAME, "password")
    ERROR_SELECTOR = (By.CSS_SELECTOR, "h3[data-test='error']")
    LOGIN_BTN_SELECTOR = (By.ID, "login-button")
    INVENTORY_ITEM_SELECTOR = (By.CLASS_NAME, "inventory_item")
