from selenium import webdriver # https://www.selenium.dev/documentation
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.relative_locator import locate_with
import unittest # https://docs.python.org/3/library/unittest.html

# https://saucelabs.com/resources/articles/selenium-4-relative-locators
class ElementLocatorsExample(unittest.TestCase):

    DEMO_APP = "https://demo.applitools.com/"

    '''
        Overrides the setUp method provided by unittest.TesCase
    '''
    def setUp(self):
        self.browser = webdriver.Chrome()
        self.browser.set_page_load_timeout(30) # seconds for page to load
        self.browser.implicitly_wait(10) # seconds for elements
        self.browser.get(self.DEMO_APP)
        self.browser.maximize_window()

    def tearDown(self):
        self.browser.quit()

    def test_css_locator(self):
        auth_header = self.browser.find_element(By.CSS_SELECTOR, "div.auth-box-w > h4.auth-header")
        self.assertEqual(auth_header.text, "Login Form")

    def test_below_relative_locator(self):
        username_label = self.browser.find_element(By.XPATH, "//label[text()='Username']")
        username_input = self.browser.find_element(locate_with(By.TAG_NAME, "input").below(username_label))
        # locate_with(By.TAG_NAME, "input").below({ By.XPATH: "//label[text()='Username']" })

        # assertions
        self.assertEqual(username_label.text, "Username")
        self.assertEqual(username_input.get_attribute("placeholder"), "Enter your username")

    def test_near_relative_locator(self):
        username_input = self.browser.find_element(
            locate_with(By.TAG_NAME, "input").near({
                By.XPATH: "//label[text()='Username']"
            })
        )

        # assertions
        self.assertEqual(username_input.get_attribute("placeholder"), "Enter your username")

    def test_create_account(self):
        if self.browser.title != "ACME demo app":
            raise InvalidState

        # login
        self.browser.find_element(By.ID, "username").send_keys("bob")
        self.browser.find_element(By.ID, "password").send_keys("test")
        self.browser.find_element(By.ID, "log-in").click()

        # verify logged in
        self.assertEqual("ACME", self.browser.find_element(By.CSS_SELECTOR, "a > div.logo-label").text)

class InvalidState(ValueError):
    """Exception raised for invalid states"""
    def __repr__(self):
        return "The state is invalid"

# Run tests
if __name__ == '__main__':
    unittest.main(verbosity=2)
