from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec


class BasePage:

    def __init__(self, driver: webdriver.Chrome):
        self.driver = driver

    @property
    def url(self) -> str:
        return "https://www.saucedemo.com"

    @property
    def explicit_wait_locator(self):
        raise NotImplemented("Locator must be implemented for each derived class.")

    def open(self):
        self.driver.get(self.url)
        WebDriverWait(self.driver, 10).until(ec.presence_of_element_located(self.explicit_wait_locator))

    def get_current_url(self) -> str:
        return self.driver.current_url