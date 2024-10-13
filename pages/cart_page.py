from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ex_con


class CartPage:
    def __init__(self, driver):
        self.driver = driver
        self.items_in_cart = (By.CSS_SELECTOR, 'div[data-test="inventory-item-name"]')
        self.continue_shopping_button = (By.CSS_SELECTOR, 'button[data-test="continue-shopping"]')
        self.checkout_button = (By.CSS_SELECTOR, 'button[data-test="checkout"]')

    def get_items_in_cart(self):
        return self.driver.find_elements(*self.items_in_cart)

    def open_page(self):
        self.driver.get("https://www.saucedemo.com/cart.html")
        WebDriverWait(self.driver, 10).until(ex_con.presence_of_element_located(
            (By.CSS_SELECTOR, "span[data-test='title']")))

    def click_continue_shopping_button(self):
        self.driver.find_element(*self.click_continue_shopping_button()).click()

    def click_checkout_button(self):
        self.driver.find_element(*self.checkout_button()).click()
