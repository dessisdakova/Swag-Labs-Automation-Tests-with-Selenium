from pages.checkout_step_two_page import CheckoutStepTwo
from pages.inventory_page import InventoryPage


def test_cancel_button_redirects_to_checkout_one_page(logged_in_driver):
    checkout_two_page = CheckoutStepTwo(logged_in_driver)
    checkout_two_page.open()

    checkout_two_page.click_cancel_button()

    assert checkout_two_page.get_current_url()== "https://www.saucedemo.com/inventory.html", \
        "User is not redirected to inventory page."


# todo
def test_finish_button_redirects_checkout_complete(logged_in_driver):
    pass


def test_correct_product_is_in_order(logged_in_driver):
    inventory_page = InventoryPage(logged_in_driver)
    inventory_page.open()
    backpack_add_button = inventory_page.get_add_to_cart_buttons()[0]
    backpack_add_button.click()

    checkout_two_page = CheckoutStepTwo(logged_in_driver)
    checkout_two_page.open()
    first_product_name = checkout_two_page.get_cart_item_names()[0]

    assert len(checkout_two_page.get_cart_item_names()) == 1, "Item was not added to the order."
    assert first_product_name == "Sauce Labs Backpack", "Different item was added to order."