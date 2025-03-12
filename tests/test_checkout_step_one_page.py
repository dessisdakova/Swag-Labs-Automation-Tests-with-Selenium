from pages.checkout_step_one_page import CheckoutStepOne


def test_cancel_button_redirects_to_cart_page(logged_in_driver):
    checkout_one_page = CheckoutStepOne(logged_in_driver)
    checkout_one_page.open()

    checkout_one_page.click_cancel_button()

    assert checkout_one_page.get_current_url()== "https://www.saucedemo.com/cart.html", \
        "User is not redirected to cart page."
