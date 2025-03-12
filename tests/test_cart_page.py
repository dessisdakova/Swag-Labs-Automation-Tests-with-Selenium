from pages.cart_page import CartPage
from pages.inventory_page import InventoryPage


def test_continue_shopping_button_redirects_to_inventory_page(logged_in_driver):
    cart_page = CartPage(logged_in_driver)
    cart_page.open()

    cart_page.click_continue_shopping_button()

    assert cart_page.get_current_url() == "https://www.saucedemo.com/inventory.html", \
        "User is not redirected to Inventory page."

def test_checkout_button_redirects_to_checkout_page(logged_in_driver):
    cart_page = CartPage(logged_in_driver)
    cart_page.open()

    cart_page.click_checkout_button()

    assert cart_page.get_current_url() == "https://www.saucedemo.com/checkout-step-one.html", \
        "User is not redirected to Checkout Step One page."


def test_correct_product_is_added_to_cart(logged_in_driver):
    inventory_page = InventoryPage(logged_in_driver)
    inventory_page.open()
    backpack_add_button = inventory_page.get_add_to_cart_buttons()[0]
    backpack_add_button.click()
    inventory_page.go_to_cart()

    cart_page = CartPage(logged_in_driver)
    cart_page.open()
    first_product_name = cart_page.get_items_in_cart()[0].text

    assert len(cart_page.get_items_in_cart()) == 1, "Item was not added to the cart."
    assert first_product_name == "Sauce Labs Backpack", "Different item was added to cart."


def test_product_can_be_removed_from_cart(logged_in_driver):
    cart_page = CartPage(logged_in_driver)
    cart_page.open()
    remove_btn = cart_page.get_remove_buttons()[0]
    remove_btn.click()

    assert len(cart_page.get_items_in_cart()) == 0, "Item was not removed from cart."
