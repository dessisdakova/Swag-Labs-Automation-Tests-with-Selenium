import unittest
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ex_con
from selenium.webdriver.support.ui import Select


class ProductsSortingTests(unittest.TestCase):

    def setUp(self):
        service = Service(ChromeDriverManager().install())
        self.driver = webdriver.Chrome(service=service)
        self.driver.get("https://www.saucedemo.com")
        self.driver.find_element(By.CSS_SELECTOR, '[data-test="username"]').send_keys("standard_user")
        self.driver.find_element(By.CSS_SELECTOR, '[data-test="password"]').send_keys("secret_sauce")
        self.driver.find_element(By.CSS_SELECTOR, "[data-test='login-button']").click()
        WebDriverWait(self.driver, 10).until(ex_con.presence_of_element_located((By.ID, "inventory_container")))

    def tearDown(self):
        self.driver.quit()

    def test_products_sort_by_name_A_to_Z(self):
        sort_dropdown = Select(self.driver.find_element(By.XPATH, "//select[@data-test='product-sort-container']"))
        sort_dropdown.select_by_visible_text("Name (A to Z)")
        products = self.driver.find_elements(By.CSS_SELECTOR, 'div[class="inventory_list"]')
        product_names = []
        for product in products:
            product_name = product.find_element(By.CSS_SELECTOR, 'div[data-test="inventory-item-name"]')
            product_names.append(product_name)
        assert product_names == sorted(product_names), "Products are not sorted alphabetically (A to Z)!"
        print("Products are sorted alphabetically (A to Z) as expected.")

    def test_products_sorted_by_name_Z_to_A(self):
        sort_dropdown = Select(self.driver.find_element(By.CSS_SELECTOR, "select[data-test='product-sort-container']"))
        sort_dropdown.select_by_visible_text("Name (Z to A)")
        products = self.driver.find_elements(By.CSS_SELECTOR, 'div[class="inventory_list"]')
        product_names = []
        for product in products:
            product_name = product.find_element(By.CSS_SELECTOR, 'div[data-test="inventory-item-name"]')
            product_names.append(product_name)

        assert product_names == sorted(product_names, reverse=True), "Products are not sorted Z to A"
        print("Products are sorted Z to A as expected")

    def test_products_sorted_by_price_low_to_high(self):
        sort_dropdown = Select(self.driver.find_element(By.CSS_SELECTOR, "select[data-test='product-sort-container']"))
        sort_dropdown.select_by_visible_text("Price (low to high)")
        products = self.driver.find_elements(By.CSS_SELECTOR, 'div[class="inventory_list"]')
        product_prices = []
        for product in products:
            product_price = product.find_element(By.CSS_SELECTOR, 'div[data-test="inventory-item-price"]').text
            product_prices.append(product_price)
        numeric_product_prices = [float(price.replace("$", "")) for price in product_prices]
        assert numeric_product_prices == sorted(numeric_product_prices), "Products are not sorted by price low to high"
        print("Products are sorted by price low to high as expected")

    def test_products_sorted_by_price_high_to_low(self):
        sort_dropdown = Select(self.driver.find_element(By.CSS_SELECTOR, "select[data-test='product-sort-container']"))
        sort_dropdown.select_by_visible_text("Price (high to low)")
        products = self.driver.find_elements(By.CSS_SELECTOR, 'div[class="inventory_list"]')
        product_prices = []
        for product in products:
            product_price = product.find_element(By.CSS_SELECTOR, 'div[data-test="inventory-item-price"]').text
            product_prices.append(product_price)
        numeric_product_prices = [float(price.replace("$", "")) for price in product_prices]
        assert numeric_product_prices == sorted(numeric_product_prices, reverse=True), \
            "Products are not sorted by price high to low"
        print("Products are sorted by price high to low as expected")


if __name__ == "__main__":
    unittest.main()
