from pages.inventory_page import InventoryPage


def test_products_sort_by_name_a_to_z(logged_in_driver):
    inventory_page = InventoryPage(logged_in_driver)
    inventory_page.open()

    inventory_page.select_sorting("Name (A to Z)")
    product_names = inventory_page.get_product_names()

    assert product_names == sorted(product_names), \
        "Products are not sorted alphabetically (A to Z)!"


def test_products_sorted_by_name_z_to_a(logged_in_driver):
    inventory_page = InventoryPage(logged_in_driver)
    inventory_page.open()

    inventory_page.select_sorting("Name (Z to A)")
    product_names = inventory_page.get_product_names()

    assert product_names == sorted(product_names, reverse=True), \
        "Products are not sorted Z to A"


def test_products_sorted_by_price_low_to_high(logged_in_driver):
    inventory_page = InventoryPage(logged_in_driver)
    inventory_page.open()

    inventory_page.select_sorting("Price (low to high)")
    product_prices = inventory_page.get_product_prices()

    assert product_prices == sorted(product_prices), \
        "Products are not sorted by price low to high"


def test_products_sorted_by_price_high_to_low(logged_in_driver):
    inventory_page = InventoryPage(logged_in_driver)
    inventory_page.open()

    inventory_page.select_sorting("Price (high to low)")
    product_prices = inventory_page.get_product_prices()

    assert product_prices == sorted(product_prices, reverse=True), \
        "Products are not sorted by price high to low"


def test_products_can_be_added_to_cart(logged_in_driver):
    inventory_page = InventoryPage(logged_in_driver)
    inventory_page.open()

    add_buttons = inventory_page.get_add_to_cart_buttons()

    for button in add_buttons:
        button.click()

    assert inventory_page.get_items_in_cart() == 6, \
        "All products have not been added to cart."


def test_products_can_be_removed_from_cart(logged_in_driver):
    inventory_page = InventoryPage(logged_in_driver)
    inventory_page.open()

    add_buttons = inventory_page.get_add_to_cart_buttons()
    for button in add_buttons:
        button.click()
    remove_buttons = inventory_page.get_remove_buttons()
    for button in remove_buttons:
        button.click()

    assert inventory_page.get_items_in_cart() == 0, \
        "All products have not been removed from cart."


def test_shopping_cart_link_redirects_to_cart(logged_in_driver):
    inventory_page = InventoryPage(logged_in_driver)
    inventory_page.open()

    inventory_page.go_to_cart()

    assert inventory_page.get_current_url() == "https://www.saucedemo.com/cart.html", \
        "User is not redirected to correct page."

