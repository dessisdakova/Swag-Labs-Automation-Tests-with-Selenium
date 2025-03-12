from selenium.webdriver.common.by import By

from pages.base_page import BasePage
from pages.burger_menu import BurgerMenu


class CheckoutStepOne(BasePage, BurgerMenu):

    first_name_field = (By.ID, "first-name")
    last_name_field = (By.ID, "last-name")
    postal_code_field = (By.ID, "postal-code")
    error_message = (By.CSS_SELECTOR, "h3[data-test='error']")
    cancel_button = (By.ID, "cancel")
    continue_button = (By.ID, "continue")
    explicit_wait_element = (By.CLASS_NAME, "checkout_info")

    def __init__(self, driver):
        super().__init__(driver)
        BurgerMenu.__init__(self, driver)

    @property
    def url(self) -> str:
        return super().url + "/checkout-step-one.html"

    @property
    def explicit_wait_locator(self):
        return CheckoutStepOne.explicit_wait_element

    def enter_first_name(self, first_name: str):
        self.driver.find_element(*CheckoutStepOne.first_name_field).send_keys(first_name)

    def enter_last_name(self, last_name: str):
        self.driver.find_element(*CheckoutStepOne.last_name_field).send_keys(last_name)

    def enter_postal_code(self, postal_code: str):
        self.driver.find_element(*CheckoutStepOne.postal_code_field).send_keys(postal_code)

    def get_error_message_text(self) -> str:
        return self.driver.find_element(*CheckoutStepOne.error_message).text

    def click_cancel_button(self):
        self.driver.find_element(*CheckoutStepOne.cancel_button).click()

    def click_continue_button(self):
        self.driver.find_element(*CheckoutStepOne.continue_button).click()