from pages.checkout_step_one_page import CheckoutStepOne


def test_cancel_button_redirects_to_cart_page(logged_in_driver):
    checkout_one_page = CheckoutStepOne(logged_in_driver)
    checkout_one_page.open()

    checkout_one_page.click_cancel_button()

    assert checkout_one_page.get_current_url()== "https://www.saucedemo.com/cart.html", \
        "User is not redirected to cart page."


def test_continue_button_redirects_user_to_step_two_if_valid_info(logged_in_driver):
    checkout_one_page = CheckoutStepOne(logged_in_driver)
    checkout_one_page.open()

    checkout_one_page.enter_first_name("John")
    checkout_one_page.enter_last_name("Doe")
    checkout_one_page.enter_postal_code("AS1234")
    checkout_one_page.click_continue_button()

    assert checkout_one_page.get_current_url() == "https://www.saucedemo.com/checkout-step-two.html", \
        "User is not redirected to step two page."


def test_continue_button_shows_error_mgs_if_missing_first_name(logged_in_driver):
    checkout_one_page = CheckoutStepOne(logged_in_driver)
    checkout_one_page.open()

    checkout_one_page.enter_last_name("Doe")
    checkout_one_page.enter_postal_code("AS1234")
    checkout_one_page.click_continue_button()

    assert checkout_one_page.get_error_message_text()== "Error: First Name is required", \
        "Incorrect or missing error message"


def test_continue_button_shows_error_mgs_if_missing_last_name(logged_in_driver):
    checkout_one_page = CheckoutStepOne(logged_in_driver)
    checkout_one_page.open()

    checkout_one_page.enter_first_name("John")
    checkout_one_page.enter_postal_code("AS1234")
    checkout_one_page.click_continue_button()

    assert checkout_one_page.get_error_message_text()== "Error: Last Name is required", \
        "Incorrect or missing error message"


def test_continue_button_shows_error_mgs_if_missing_postal_code(logged_in_driver):
    checkout_one_page = CheckoutStepOne(logged_in_driver)
    checkout_one_page.open()

    checkout_one_page.enter_first_name("John")
    checkout_one_page.enter_last_name("Doe")
    checkout_one_page.click_continue_button()

    assert checkout_one_page.get_error_message_text()== "Error: Postal Code is required", \
        "Incorrect or missing error message"
