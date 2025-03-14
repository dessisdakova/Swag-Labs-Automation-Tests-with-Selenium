from selenium.webdriver.common.by import By

from pages.base_page import BasePage
from pages.burger_menu import BurgerMenu


class CheckoutStepTwo(BasePage, BurgerMenu):
    """Page object for the Checkout Step Two page."""

    cart_item_names = (By.CSS_SELECTOR, "div[data-test='inventory-item-name']")
    total_price_label = (By.CSS_SELECTOR, "div[data-test='total-label']")
    cancel_button = (By.ID, "cancel")
    finish_button = (By.ID, "finish")
    explicit_wait_element = (By.CLASS_NAME, "summary_info")

    def __init__(self, driver):
        super().__init__(driver)
        BurgerMenu.__init__(self, driver)

    @property
    def url(self) -> str:
        return super().url + "/checkout-step-two.html"

    @property
    def explicit_wait_locator(self):
        return self.explicit_wait_element

    def get_cart_item_names(self) -> list[str]:
        """Returns a list of product names from the order."""
        elements = self._get_multiple_elements(self.cart_item_names)
        return [element.text for element in elements]

    def click_cancel_button(self):
        self._click_button(self.cancel_button)

    def click_finish_button(self):
        self._click_button(self.finish_button)
