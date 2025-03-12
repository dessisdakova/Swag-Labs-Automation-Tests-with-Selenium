from pages.cart_page import CartPage
from pages.checkout_step_one_page import CheckoutStepOne
from pages.inventory_page import InventoryPage


def test_can_be_opened_in_inventory_page(logged_in_driver):
    inventory_page = InventoryPage(logged_in_driver)
    inventory_page.open()

    inventory_page.open_menu()

    assert inventory_page.get_nav_element_visibility(), \
        "Burger menu is not opened in inventory page.."


def test_can_be_opened_in_cart_page(logged_in_driver):
    cart_page = CartPage(logged_in_driver)
    cart_page.open()

    cart_page.open_menu()

    assert cart_page.get_nav_element_visibility(), \
        "Burger menu is not opened in cart page."


def test_can_be_opened_in_checkout_step_one_page(logged_in_driver):
    checkout_one_page = CheckoutStepOne(logged_in_driver)
    checkout_one_page.open()

    checkout_one_page.open_menu()

    assert checkout_one_page.get_nav_element_visibility(), \
        "Burger menu is not opened in checkout step one page."