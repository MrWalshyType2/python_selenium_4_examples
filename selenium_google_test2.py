from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

# Open browser and setup
URL = "https://google.com"
browser = webdriver.Chrome()
browser.set_page_load_timeout(30) # seconds for page to load
browser.implicitly_wait(10) # seconds for elements
browser.get(URL)
browser.maximize_window()

# Print some info
print(f"\tURL  :", URL)
print()

# Find an element
accept_cookies_btn = browser.find_element(By.XPATH, "//button[div[text()='Accept all']]")
search_bar = browser.find_element(By.NAME, "q")

# Accept cookies
accept_cookies_btn.click()

# Interact with search bar
search_bar.send_keys("kittens" + Keys.ENTER)

# Assertions
try:
    assert "kittens - Google Search" == browser.title, "Page title mismatch"
except AssertionError:
    # assertion failed
    print("Assertion/test failure, cleaning up...")
except:
    print("Something went wrong")
finally:
    # Close the browser
    browser.quit() # close() for a tab, quits if last tab in browser
