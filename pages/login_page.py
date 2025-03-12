from selenium.webdriver.common.by import By

from pages.base_page import BasePage


class LoginPage(BasePage):

    username_field = (By.CSS_SELECTOR, '[data-test="username"]')
    password_field = (By.CSS_SELECTOR, '[data-test="password"]')
    login_button = (By.CSS_SELECTOR, "[data-test='login-button']")
    error_message = (By.CSS_SELECTOR, "[data-test='error']")
    explicit_wait_element = (By.CSS_SELECTOR, "div.login_credentials_wrap")

    def __init__(self, driver):
        super().__init__(driver)

    @property
    def explicit_wait_locator(self) -> tuple[str, str]:
        return LoginPage.explicit_wait_element

    def login(self, username, password):
        self.driver.find_element(*self.username_field).send_keys(username)
        self.driver.find_element(*self.password_field).send_keys(password)
        self.driver.find_element(*self.login_button).click()

    def get_error_message_text(self) -> str:
         return self.driver.find_element(*self.error_message).text
