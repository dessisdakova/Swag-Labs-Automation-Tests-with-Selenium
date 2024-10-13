from tests.base_test import BaseTest
from pages.login_page import LoginPage
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ex_con
import time


class LoginPageTests(BaseTest):
    def test_login_correct_credentials_should_login_successfully(self):
        login_page = LoginPage(self.driver)
        login_page.login("standard_user", "secret_sauce")
        WebDriverWait(self.driver, 10).until(ex_con.presence_of_element_located((By.ID, "inventory_container")))

        expected_url = "https://www.saucedemo.com/inventory.html"
        actual_url = self.driver.current_url
        assert actual_url == expected_url, f"URLs don't match "
        print("URL assertion passed: The URL has changed successfully.")

    def test_login_incorrect_password_should_show_error_message(self):
        login_page = LoginPage(self.driver)
        login_page.login("standard_user", "invalidPassword")

        actual = login_page.get_error_message()
        expected = "Epic sadface: Username and password do not match any user in this service"
        assert actual == expected, "Error message isn't present or doesn't match"
        print("Error message assertion passed: Message for incorrect credentials is present and matches.")

    def test_login_locked_out_user_should_show_error_message(self):
        login_page = LoginPage(self.driver)
        login_page.login("locked_out_user", "secret_sauce")

        actual = login_page.get_error_message()
        expected = "Epic sadface: Sorry, this user has been locked out."
        assert actual == expected, "Error message isn't present or doesn't match"
        print("Error message assertion passed: Message for locked out user is present and matches.")

    def test_login_performance_glitch_user_should_login_slower(self):
        # Test for the standard user
        login_page_standard = LoginPage(self.driver)
        start_time = time.time()
        login_page_standard.login("standard_user", "secret_sauce")
        WebDriverWait(self.driver, 10).until(ex_con.presence_of_element_located((By.ID, "inventory_container")))
        standard_user_login_time = time.time() - start_time
        print(f"Standard User Login Time: {standard_user_login_time:.2f} seconds")

        # Close the current session and start a new one for the performance glitch user
        self.tearDown()
        self.setUp()

        # Test for the performance glitch user
        login_page_performance_glitch = LoginPage(self.driver)
        start_time = time.time()
        login_page_performance_glitch.login("performance_glitch_user", "secret_sauce")
        WebDriverWait(self.driver, 10).until(ex_con.presence_of_element_located((By.ID, "inventory_container")))
        performance_glitch_user_login_time = time.time() - start_time
        print(f"Performance Glitch User Login Time: {performance_glitch_user_login_time:.2f} seconds")

        # Assert that the performance glitch user login time is greater than the standard user login time
        assert performance_glitch_user_login_time > standard_user_login_time, \
            "Login time for performance_glitch_user is not lower"
        print("Login time comparison passed: standard_user logs in faster than performance_glitch_user")
