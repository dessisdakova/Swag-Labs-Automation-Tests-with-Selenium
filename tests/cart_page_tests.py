from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage
from pages.cart_page import CartPage
from tests.old_base_test import BaseTest
from selenium.webdriver.common.by import By


class CartPageTests(BaseTest):
    def test_adding_items_to_cart(self):
        login_page = LoginPage(self.driver)
        login_page.login("standard_user", "secret_sauce")

        inventory_page = InventoryPage(self.driver)
        inventory_page.open_page()
        self.driver.find_element(By.CSS_SELECTOR, "button[data-test='add-to-cart-sauce-labs-backpack']").click()
        self.driver.find_element(By.CSS_SELECTOR, "button[data-test='add-to-cart-sauce-labs-bike-light']").click()

        inventory_page.go_to_cart()
        cart_page = CartPage(self.driver)
        products_in_cart = cart_page.get_items_in_cart()
        first_product_name = products_in_cart[0].text
        second_product_name = products_in_cart[1].text

        assert len(products_in_cart) == 2, "Item was not added to the cart."
        assert first_product_name == "Sauce Labs Backpack", "Different item was added to cart"
        assert second_product_name == "Sauce Labs Bike Light", "Different item was added to cart"
        print("Assertions passed: Selected items were added to the cart.")
