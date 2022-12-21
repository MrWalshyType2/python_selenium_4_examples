from selenium import webdriver # https://www.selenium.dev/documentation
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import unittest # https://docs.python.org/3/library/unittest.html

class NavigationExample(unittest.TestCase):

    URL = "https://google.com"

    '''
        Overrides the setUp method provided by unittest.TesCase
    '''
    def setUp(self):
        self.browser = webdriver.Chrome()
        self.browser.set_page_load_timeout(30) # seconds for page to load
        self.browser.implicitly_wait(10) # seconds for elements
        self.browser.get(self.URL)
        self.browser.maximize_window()

    def tearDown(self):
        self.browser.quit()

    def accept_cookies(self):
        accept_cookies_btn = self.browser.find_element(By.XPATH, "//button[div[text()='Accept all']]")
        # Accept cookies
        accept_cookies_btn.click()

    def test_navigation(self):
        self.accept_cookies()

        # go back a page
        self.browser.back()

        # go forward a page
        self.browser.forward()

        # refresh page
        self.browser.refresh()
        
        self.assertEqual("Google", self.browser.title)

# Run tests
if __name__ == '__main__':
    unittest.main(verbosity=2)
