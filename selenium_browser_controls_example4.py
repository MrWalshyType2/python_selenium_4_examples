from selenium import webdriver # https://www.selenium.dev/documentation
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
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

    '''
        Uses JavaScript executor for opening a tab (compatible with Selenium < 4)
    '''
    def test_new_tab_example(self):
        wait = WebDriverWait(self.browser, 10)
        self.accept_cookies()

        # get identifier for current tab
        original_tab = self.browser.current_window_handle # unique window handle ID

        # open a new tab by executing JS and wait for it to open
        self.browser.execute_script("window.open('https://bing.com')")
        wait.until(EC.number_of_windows_to_be(2))

        # switch to new tab
        self.browser.switch_to.window(self.browser.window_handles[1])

        # close current tab
        self.browser.close()

        # return to original tab
        self.browser.switch_to.window(original_tab)

        self.assertEqual("Google", self.browser.title)

    '''
        Selenium 4 compatible way of opening a new tab
    '''
    def test_new_tab_example2(self):
        wait = WebDriverWait(self.browser, 10)
        self.accept_cookies()

        # get identifier for current tab
        original_tab = self.browser.current_window_handle # unique window handle ID

        # open a new tab and switch to it
        self.browser.switch_to.new_window("tab")
        wait.until(EC.number_of_windows_to_be(2))

        # close current tab
        self.browser.close()

        # return to original tab
        self.browser.switch_to.window(original_tab)

        self.assertEqual("Google", self.browser.title)

    '''
        Selenium 4 compatible way of opening a new browser window
    '''
    def test_new_window_example(self):
        self.accept_cookies()

        # get identifier for current tab
        original_tab = self.browser.current_window_handle # unique window handle ID

        # open a new window and switch to it
        self.browser.switch_to.new_window("window")

        # close current window
        self.browser.close()

        # return to original window
        self.browser.switch_to.window(original_tab)

        self.assertEqual("Google", self.browser.title)

    def test_resize_window_example(self):
        self.accept_cookies()

        # window sizes
        mobile_window_size = (520, 850)
        tablet_window_size = (780, 1024)
        desktop_window_size = (1024, 720)

        # get original size
        original_window_size = self.browser.get_window_size()
        original_width = original_window_size.get("width")
        original_height = original_window_size.get("height")
        
        # change to mobile size
        self.browser.set_window_size(mobile_window_size[0], mobile_window_size[1])
        new_size = self.browser.get_window_size()
        self.assertEqual(new_size.get("width"), mobile_window_size[0])
        self.assertEqual(new_size.get("height"), mobile_window_size[1])

        # change to tablet size
        self.browser.set_window_size(tablet_window_size[0], tablet_window_size[1])
        new_size = self.browser.get_window_size()
        self.assertEqual(new_size.get("width"), tablet_window_size[0])
        self.assertEqual(new_size.get("height"), tablet_window_size[1])

        # change to desktop size
        self.browser.set_window_size(desktop_window_size[0], desktop_window_size[1])
        new_size = self.browser.get_window_size()
        self.assertEqual(new_size.get("width"), desktop_window_size[0])
        self.assertEqual(new_size.get("height"), desktop_window_size[1])

    def test_screenshot_example(self):
        self.accept_cookies()
        search_bar = self.browser.find_element(By.NAME, "q")
        search_bar.send_keys("kittens")
        # take a screenshot of the search bar with text in it
        search_bar.screenshot("./search_bar.png")

        # take a screenshot of the page
        search_bar.send_keys(Keys.ENTER)
        self.browser.save_screenshot("./search_result.png")

        self.assertEqual("kittens - Google Search", self.browser.title)

# Run tests
if __name__ == '__main__':
    unittest.main(verbosity=2)
