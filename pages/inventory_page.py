from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ex_con
from selenium.webdriver.support.ui import Select


class InventoryPage:
    def __init__(self, driver):
        self.driver = driver
        self.shopping_cart_link = (By.CSS_SELECTOR, 'a[data-test="shopping-cart-link"]')
        self.product_names = (By.CSS_SELECTOR, 'div[data-test="inventory-item-name"]')
        self.product_prices = (By.CSS_SELECTOR, 'div[data-test="inventory-item-price"]')
        self.sorting_drop_down = (By.XPATH, "//select[@data-test='product-sort-container']")

    def open_page(self):
        self.driver.get("https://www.saucedemo.com/inventory.html")
        WebDriverWait(self.driver, 10).until(ex_con.presence_of_element_located((By.ID, "inventory_container")))

    def get_product_names(self):
        elements = self.driver.find_elements(*self.product_names)
        return [element.text for element in elements]

    def get_product_prices(self):
        elements = self.driver.find_elements(*self.product_prices)
        return [float(element.text.replace("$", "").strip()) for element in elements]

    def select_sorting(self, option):
        dropdown = Select(self.driver.find_element(*self.sorting_drop_down))
        dropdown.select_by_visible_text(option)

    def go_to_cart(self):
        self.driver.find_element(*self.shopping_cart_link).click()
