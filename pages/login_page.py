from selenium.common import TimeoutException
from selenium.webdriver.common.by import By

from pages.base_page import BasePage


class LoginPage(BasePage):
    """Page object for the Login page."""

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
        self._enter_text_to_field(self.username_field, username)
        self._enter_text_to_field(self.password_field, password)
        self._click_button(self.login_button)

    def get_error_message_text(self) -> str:
        return self._get_text(self.error_message)

    def is_login_successful(self) -> bool:
        """Check if login was successful by verifying the absence of the login button."""
        try:
            self._wait_for_invisibility_of_element(self.login_button)
            return True
        except TimeoutException:
            return False
