from pages.cart_page import CartPage
from pages.inventory_page import InventoryPage


def test_can_be_opened_in_inventory_page(logged_in_driver):
    inventory_page = InventoryPage(logged_in_driver)
    inventory_page.open()

    inventory_page.open_menu()

    assert inventory_page.get_nav_element_visibility()


def test_can_be_opened_in_cart_page(logged_in_driver):
    cart_page = CartPage(logged_in_driver)
    cart_page.open()

    cart_page.open_menu()

    assert cart_page.get_nav_element_visibility()