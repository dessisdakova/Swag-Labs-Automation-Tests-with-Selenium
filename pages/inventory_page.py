from selenium.common import StaleElementReferenceException
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support.ui import Select

from pages.base_page import BasePage
from pages.burger_menu import BurgerMenu


class InventoryPage(BasePage, BurgerMenu):

    shopping_cart_link = (By.CSS_SELECTOR, 'a[data-test="shopping-cart-link"]')
    add_to_card_buttons = (By.CSS_SELECTOR, "button.btn_inventory")
    remove_buttons = (By.CSS_SELECTOR, "button.btn_secondary")
    product_names = (By.CSS_SELECTOR, 'div[data-test="inventory-item-name"]')
    product_prices = (By.CSS_SELECTOR, 'div[data-test="inventory-item-price"]')
    sorting_drop_down_menu = (By.XPATH, "//select[@data-test='product-sort-container']")
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

    def get_product_names(self):
        elements = self.driver.find_elements(*InventoryPage.product_names)
        return [element.text for element in elements]

    def get_product_prices(self):
        elements = self.driver.find_elements(*InventoryPage.product_prices)
        return [float(element.text.replace("$", "").strip()) for element in elements]

    def select_sorting(self, option):
        dropdown = Select(self.driver.find_element(*InventoryPage.sorting_drop_down_menu))
        dropdown.select_by_visible_text(option)

    def get_add_to_cart_buttons(self) -> list[WebElement]:
        return self.driver.find_elements(*InventoryPage.add_to_card_buttons)

    def get_remove_buttons(self) -> list[WebElement]:
        return self.driver.find_elements(*InventoryPage.remove_buttons)

    def go_to_cart(self):
        self.driver.find_element(*InventoryPage.shopping_cart_link).click()

    def get_items_in_cart(self) -> int:
        try:
            return int(self.driver.find_element(*InventoryPage.shopping_cart_link).text)
        except ValueError:
            return 0
