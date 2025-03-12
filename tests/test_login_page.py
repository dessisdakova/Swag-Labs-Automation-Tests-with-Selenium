import time

from pages.inventory_page import InventoryPage
from pages.login_page import LoginPage


def test_login_correct_credentials_should_login_successfully(driver):
    login_page = LoginPage(driver)
    login_page.open()
    login_page.login("standard_user", "secret_sauce")

    assert login_page.get_current_url() == "https://www.saucedemo.com/inventory.html", \
        "User is not redirected to correct page."


def test_login_incorrect_password_should_show_error_message(driver):
    expected_error_msg = "Epic sadface: Username and password do not match any user in this service"

    login_page = LoginPage(driver)
    login_page.open()
    login_page.login("standard_user", "invalidPassword")

    assert login_page.get_error_message_text() == expected_error_msg, \
        "Error message isn't present or doesn't equal expected."


def test_login_locked_out_user_should_show_error_message(driver):
    expected_error_msg = "Epic sadface: Sorry, this user has been locked out."

    login_page = LoginPage(driver)
    login_page.open()
    login_page.login("locked_out_user", "secret_sauce")

    assert login_page.get_error_message_text() == expected_error_msg, \
        "Error message isn't present or doesn't equal expected."


def test_login_performance_glitch_user_should_login_slower(driver):
    login_page = LoginPage(driver)
    login_page.open()
    login_page.login("standard_user", "secret_sauce")

    start_time = time.time()
    InventoryPage(driver).open()
    standard_user_login_time = time.time() - start_time
    print(f"Standard User Login Time: {standard_user_login_time:.2f} seconds")

    login_page.open()
    login_page.login("performance_glitch_user", "secret_sauce")
    start_time = time.time()
    InventoryPage(driver).open()
    performance_glitch_user_login_time = time.time() - start_time
    print(f"Performance Glitch User Login Time: {performance_glitch_user_login_time:.2f} seconds")

    assert performance_glitch_user_login_time > standard_user_login_time, \
        "Login time for performance_glitch_user is not lower."