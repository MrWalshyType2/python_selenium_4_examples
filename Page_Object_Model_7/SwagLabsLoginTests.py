from selenium import webdriver # https://www.selenium.dev/documentation
from WebDriverTest import WebDriverTest
from SwagLabsLoginPage import LoginPage
from LoginLandingPage import LoginLandingPage
from LoginErrorPage import LoginErrorPage
import unittest

class SwagLabsLoginTests(WebDriverTest):

    URL = "https://www.saucedemo.com/"

    def test_login_success(self):
        self.driver.get(self.URL)
        
        # Arrange
        username = "standard_user"
        password = "secret_sauce"

        # Act
        login_page = LoginPage(self.driver)
        login_page.login(username, password)
        login_landing_page = LoginLandingPage(self.driver)

        # Assert
        self.assertTrue(login_landing_page.did_products_load())

    def test_login_locked_out_user(self):
        self.driver.get(self.URL)
        
        # Arrange
        username = "locked_out_user"
        password = "secret_sauce"
        expected_error_message = "Epic sadface: Sorry, this user has been locked out."

        # Act
        login_page = LoginPage(self.driver)
        login_page.login(username, password)
        login_error_page = LoginErrorPage(self.driver)

        # Assert
        self.assertEqual(login_error_page.get_error_message(), expected_error_message)

    def test_login_wrong_password(self):
        self.driver.get(self.URL)
        
        # Arrange
        username = "problem_user"
        password = "wrong"
        expected_error_message = "Epic sadface: Username and password do not match any user in this service"

        # Act
        login_page = LoginPage(self.driver)
        login_page.login(username, password)
        login_error_page = LoginErrorPage(self.driver)

        # Assert
        self.assertEqual(login_error_page.get_error_message(), expected_error_message)

if __name__ == '__main__':
    unittest.main(verbosity=2)
