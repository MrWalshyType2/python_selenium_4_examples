from selenium import webdriver # https://www.selenium.dev/documentation
import unittest

class WebDriverTest(unittest.TestCase):

    def setUp(self):
        print("\nSetting up test environment")
        self.driver = webdriver.Chrome()
        self.driver.set_page_load_timeout(30)
        self.driver.implicitly_wait(10)
        self.driver.maximize_window()

    def tearDown(self):
        if (self.driver != None):
            print("Cleaning up test environment")
            self.driver.quit()
