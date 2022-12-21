from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

# Open browser and setup
URL = "https://automatetheboringstuff.com"
browser = webdriver.Chrome()
browser.get(URL)
browser.maximize_window()

# Print some info
title = browser.title
print(f"\n\tTitle:", title)
print(f"\tURL  :", URL)
print()

# Find an element
mainHeading1 = browser.find_element(By.CSS_SELECTOR, "main h1")

# Assertions
try:
    assert "Automate the Boring Stuff with Python" == title, "Page title mismatch"
    assert "Automate the Boring Stuff with Python" == mainHeading1.text, "Page main h1 mismatch"
except AssertionError:
    # assertion failed
    print("Assertion/test failure, cleaning up...")

# Close the browser
browser.quit() # close() for a tab, quits if last tab in browser
