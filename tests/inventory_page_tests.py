from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage
from tests.base_test import BaseTest


class InventoryPageTests(BaseTest):
    def test_products_sort_by_name_A_to_Z(self):
        login_page = LoginPage(self.driver)
        login_page.login("standard_user", "secret_sauce")
        inventory_page = InventoryPage(self.driver)

        inventory_page.select_sorting("Name (A to Z)")
        product_names = inventory_page.get_product_names()

        assert product_names == sorted(product_names), "Products are not sorted alphabetically (A to Z)!"
        print("Products are sorted alphabetically (A to Z) as expected.")

    def test_products_sorted_by_name_Z_to_A(self):
        login_page = LoginPage(self.driver)
        login_page.login("standard_user", "secret_sauce")
        inventory_page = InventoryPage(self.driver)

        inventory_page.select_sorting("Name (Z to A)")
        product_names = inventory_page.get_product_names()

        assert product_names == sorted(product_names, reverse=True), "Products are not sorted Z to A"
        print("Products are sorted Z to A as expected")

    def test_products_sorted_by_price_low_to_high(self):
        login_page = LoginPage(self.driver)
        login_page.login("standard_user", "secret_sauce")
        inventory_page = InventoryPage(self.driver)

        inventory_page.select_sorting("Price (low to high)")
        product_prices = inventory_page.get_product_prices()

        assert product_prices == sorted(product_prices), "Products are not sorted by price low to high"
        print("Products are sorted by price low to high as expected")

    def test_products_sorted_by_price_high_to_low(self):
        login_page = LoginPage(self.driver)
        login_page.login("standard_user", "secret_sauce")
        inventory_page = InventoryPage(self.driver)

        inventory_page.select_sorting("Price (high to low)")
        product_prices = inventory_page.get_product_prices()

        assert product_prices == sorted(product_prices, reverse=True), "Products are not sorted by price high to low"
        print("Products are sorted by price high to low as expected")
