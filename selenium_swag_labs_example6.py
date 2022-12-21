from selenium import webdriver # https://www.selenium.dev/documentation
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import unittest # https://docs.python.org/3/library/unittest.html

class SwagLabsExample(unittest.TestCase):

    SAUCE_DEMO_URL = "https://www.saucedemo.com/"
    USERNAME_SELECTOR = (By.NAME, "user-name")
    PASSWORD_SELECTOR = (By.NAME, "password")
    ERROR_SELECTOR = (By.CSS_SELECTOR, "h3[data-test='error']")
    LOGIN_BTN_SELECTOR = (By.ID, "login-button")
    INVENTORY_ITEM_SELECTOR = (By.CLASS_NAME, "inventory_item")

    '''
        Overrides the setUp method provided by unittest.TesCase
    '''
    def setUp(self):
        self.browser = webdriver.Chrome()
        self.browser.set_page_load_timeout(30) # seconds for page to load
        self.browser.implicitly_wait(10) # seconds for elements
        self.browser.get(self.SAUCE_DEMO_URL)
        self.browser.maximize_window()

    def tearDown(self):
        self.browser.quit()

    def login(self, username, password):
        self.browser.find_element(self.USERNAME_SELECTOR[0], self.USERNAME_SELECTOR[1]).send_keys(username)
        self.browser.find_element(self.PASSWORD_SELECTOR[0], self.PASSWORD_SELECTOR[1]).send_keys(password)
        self.browser.find_element(self.LOGIN_BTN_SELECTOR[0], self.LOGIN_BTN_SELECTOR[1]).click()

    def test_login_success(self):
        # Arrange
        username = "standard_user"
        password = "secret_sauce"

        # Act
        self.login(username, password)

        # Assert
        products = self.browser.find_elements(self.INVENTORY_ITEM_SELECTOR[0], self.INVENTORY_ITEM_SELECTOR[1])
        self.assertTrue(len(products) > 0)

    def test_login_locked_out_user(self):
        # Arrange
        username = "locked_out_user"
        password = "secret_sauce"
        expected_error_message = "Epic sadface: Sorry, this user has been locked out."

        # Act
        self.login(username, password)

        # Assert
        error = self.browser.find_element(self.ERROR_SELECTOR[0], self.ERROR_SELECTOR[1])
        self.assertEqual(expected_error_message, error.text)

    def test_login_wrong_password(self):
        # Arrange
        username = "problem_user"
        password = "wrong"
        expected_error_message = "Epic sadface: Username and password do not match any user in this service"

        # Act
        self.login(username, password)

        # Assert
        error = self.browser.find_element(self.ERROR_SELECTOR[0], self.ERROR_SELECTOR[1])
        self.assertEqual(expected_error_message, error.text)

class InvalidState(ValueError):
    """Exception raised for invalid states"""
    def __repr__(self):
        return "The state is invalid"

# Run tests
if __name__ == '__main__':
    unittest.main(verbosity=2)
