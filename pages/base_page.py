from selenium import webdriver
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec


class BasePage:

    def __init__(self, driver: webdriver.Chrome):
        self.driver = driver

    @property
    def url(self) -> str:
        """Returns the URL of page."""
        return "https://www.saucedemo.com"

    @property
    def explicit_wait_locator(self):
        """Returns the locator for the explicit wait element."""
        raise NotImplemented("Locator must be implemented for each derived class.")

    def open(self):
        """Open the page and wait for the explicit wait locator to be present."""
        self.driver.get(self.url)
        WebDriverWait(self.driver, 5).until(ec.presence_of_element_located(self.explicit_wait_locator))

    def get_current_url(self) -> str:
        """Returns the current URL of the page."""
        return self.driver.current_url

    def _enter_text_to_field(self, locator: tuple[str, str], text: str):
        """Enter text into a specified field."""
        self.driver.find_element(*locator).send_keys(text)

    def _click_button(self, locator: tuple[str, str]):
        """Click the specified button."""
        self.driver.find_element(*locator).click()

    def _get_text(self, locator: tuple[str, str]) -> str:
        """Returns the text of the specified element."""
        return self.driver.find_element(*locator).text

    def _get_multiple_elements(self, locator: tuple[str, str]) -> list[WebElement]:
        """Returns a list of WebElements matching the specified locator."""
        return self.driver.find_elements(*locator)

    def _select_dropdown_option(self, locator: tuple[str, str], option: str):
        """Select an option from a dropdown menu."""
        dropdown = Select(self.driver.find_element(*locator))
        dropdown.select_by_visible_text(option)

    def _wait_for_invisibility_of_element(self, locator: tuple[str, str]):
        """Wait for an element to be invisibly or not present."""
        WebDriverWait(self.driver, 5).until(ec.invisibility_of_element_located(locator))
