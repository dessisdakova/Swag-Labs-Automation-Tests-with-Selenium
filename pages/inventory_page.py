from selenium.webdriver.common.by import By

from pages.base_page import BasePage
from pages.burger_menu import BurgerMenu


class InventoryPage(BasePage, BurgerMenu):
    """Page object for the Inventory page."""

    shopping_cart_link = (By.CSS_SELECTOR, 'a[data-test="shopping-cart-link"]')
    add_to_card_buttons = (By.CSS_SELECTOR, "button.btn_inventory")
    remove_buttons = (By.CSS_SELECTOR, "button.btn_secondary")
    product_names_labels = (By.CSS_SELECTOR, 'div[data-test="inventory-item-name"]')
    product_prices_labels = (By.CSS_SELECTOR, 'div[data-test="inventory-item-price"]')
    drop_down_menu_for_sorting = (By.XPATH, "//select[@data-test='product-sort-container']")
    explicit_wait_element = (By.ID, "inventory_container")

    def __init__(self, driver):
        super().__init__(driver)
        BurgerMenu.__init__(self, driver)

    @property
    def url(self) -> str:
        return super().url + "/inventory.html"

    @property
    def explicit_wait_locator(self):
        return InventoryPage.explicit_wait_element

    def get_product_names(self) -> list[str]:
        """Returns a list of product names from the inventory."""
        elements = self._get_multiple_elements(self.product_names_labels)
        return [element.text for element in elements]

    def get_product_prices(self) -> list[float]:
        """Returns a list of product prices from the inventory."""
        elements = self._get_multiple_elements(self.product_prices_labels)
        return [float(element.text.replace("$", "").strip()) for element in elements]

    def select_sorting(self, option):
        self._select_dropdown_option(self.drop_down_menu_for_sorting, option)

    def get_add_to_cart_buttons(self):
        return self._get_multiple_elements(self.add_to_card_buttons)

    def get_remove_buttons(self):
        return self._get_multiple_elements(self.remove_buttons)

    def go_to_cart(self):
        self._click_button(self.shopping_cart_link)

    def get_items_in_cart(self) -> int:
        """Returns the number of items in the cart, or 0 if the cart is empty."""
        try:
            return int(self._get_text(self.shopping_cart_link))
        except ValueError:
            return 0
