from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement

from pages.base_page import BasePage
from pages.burger_menu import BurgerMenu


class CartPage(BasePage, BurgerMenu):

    items_in_cart = (By.CSS_SELECTOR, 'div[data-test="inventory-item-name"]')
    remove_buttons = (By.CSS_SELECTOR, "button.btn_small")
    continue_shopping_button = (By.CSS_SELECTOR, 'button[data-test="continue-shopping"]')
    checkout_button = (By.CSS_SELECTOR, 'button[data-test="checkout"]')
    explicit_wait_element = (By.CSS_SELECTOR, "span[data-test='title']")

    def __init__(self, driver):
        super().__init__(driver)
        BurgerMenu.__init__(self, driver)

    @property
    def url(self) -> str:
        return super().url + "/cart.html"

    @property
    def explicit_wait_locator(self) -> tuple[str, str]:
        return CartPage.explicit_wait_element

    def get_items_in_cart(self) -> list[WebElement]:
        return self.driver.find_elements(*CartPage.items_in_cart)

    def click_continue_shopping_button(self):
        self.driver.find_element(*CartPage.continue_shopping_button).click()

    def click_checkout_button(self):
        self.driver.find_element(*CartPage.checkout_button).click()

    def get_remove_buttons(self) ->list[WebElement]:
        return self.driver.find_elements(*CartPage.remove_buttons)