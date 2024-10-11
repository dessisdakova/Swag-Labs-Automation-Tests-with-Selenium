import unittest
import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ex_con
from webdriver_manager.chrome import ChromeDriverManager


class LoginTests(unittest.TestCase):

    def setUp(self):
        service = Service(ChromeDriverManager().install())
        self.driver = webdriver.Chrome(service=service)
        self.driver.get("https://www.saucedemo.com")

    def tearDown(self):
        self.driver.quit()

    def test_login_correct_credentials_should_login_successfully(self):
        # arrange
        username_field = self.driver.find_element(By.CSS_SELECTOR, '[data-test="username"]')
        username_field.send_keys("standard_user")
        password_field = self.driver.find_element(By.CSS_SELECTOR, '[data-test="password"]')
        password_field.send_keys("secret_sauce")
        login_button = self.driver.find_element(By.CSS_SELECTOR, "[data-test='login-button']")

        # act
        login_button.click()
        WebDriverWait(self.driver, 10).until(ex_con.presence_of_element_located((By.ID, "inventory_container")))

        # assert
        expected_url = "https://www.saucedemo.com/inventory.html"
        actual_url = self.driver.current_url
        assert actual_url == expected_url, f"URLs don't match "
        print("URL assertion passed: The URL has changed successfully.")

    def test_login_incorrect_password_should_show_error_message(self):
        # arrange
        username_field = self.driver.find_element(By.CSS_SELECTOR, '[data-test="username"]')
        username_field.send_keys("standard_user")
        password_field = self.driver.find_element(By.CSS_SELECTOR, '[data-test="password"]')
        password_field.send_keys("invalidPassword")

        # act
        self.driver.find_element(By.CSS_SELECTOR, "[data-test='login-button']").click()
        WebDriverWait(self.driver, 10).until(ex_con.presence_of_element_located((By.ID, "inventory_container")))

        # assert
        error_message = self.driver.find_element(By.CSS_SELECTOR, "[data-test='error']")
        actual = error_message.text
        expected = "Epic sadface: Username and password do not match any user in this service"
        assert actual == expected
        print("Error message assertion passed: Message for incorrect credentials is present.")

    def test_login_locked_out_user_should_show_error_message(self):
        # arrange
        locked_user = "locked_out_user"
        password = "secret_sauce"
        self.driver.find_element(By.CSS_SELECTOR, '[data-test="username"]').send_keys(locked_user)
        self.driver.find_element(By.CSS_SELECTOR, '[data-test="password"]').send_keys(password)

        # act
        self.driver.find_element(By.CSS_SELECTOR, "[data-test='login-button']").click()
        WebDriverWait(self, 10).until(ex_con.presence_of_element_located((By.ID, "inventory_container")))

        # assert
        error_message = self.driver.find_element(By.CSS_SELECTOR, "[data-test='error']")
        actual = error_message.text
        expected = "Epic sadface: Sorry, this user has been locked out."
        assert actual == expected
        print("Error message assertion passed: Message for locked out user is present.")

    # Helper method to perform login for performance_glitch_user.
    def login(self, username, password):
        self.driver.find_element(By.CSS_SELECTOR, '[data-test="username"]').send_keys(username)
        self.driver.find_element(By.CSS_SELECTOR, '[data-test="password"]').send_keys(password)
        self.driver.find_element(By.CSS_SELECTOR, "[data-test='login-button']").click()
        WebDriverWait(self.driver, 10).until(ex_con.presence_of_element_located((By.ID, "inventory_container")))

    def test_login_performance_glitch_user_should_login_slower(self):
        # arrange + act
        start_time = time.time()
        self.login("standard_user", "secret_sauce")
        standard_user_login_time = time.time() - start_time
        print(f"Standard User Login Time: {standard_user_login_time:.2f} seconds")
        self.tearDown()

        self.setUp()
        start_time = time.time()
        self.login("performance_glitch_user", "secret_sauce")
        performance_glitch_user_login_time = time.time() - start_time
        print(f"Performance Glitch User Login Time: {performance_glitch_user_login_time:.2f} seconds")

        # assert
        assert performance_glitch_user_login_time > standard_user_login_time, f"Login time for " \
                                                                              f"performance_glitch_user is not lower"
        print("Login time comparison passed: standard_user logs in faster than performance_glitch_user")


if __name__ == "__main__":
    unittest.main()
