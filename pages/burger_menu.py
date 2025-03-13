from selenium.common import TimeoutException
from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec


class BurgerMenu:
    """Page object for the Burger Menu."""

    nav_bar = (By.TAG_NAME, "nav")
    main_icon = (By.ID, "react-burger-menu-btn")
    all_items = (By.ID, "inventory_sidebar_link")
    about = (By.ID, "about_sidebar_link")
    log_out = (By.ID, "logout_sidebar_link")
    reset_app_state = (By.ID, "reset_sidebar_link")
    exit = (By.ID, "react-burger-cross-btn")

    def __init__(self, driver:webdriver.Chrome):
        self.driver = driver

    def open_menu(self):
        self.driver.find_element(*BurgerMenu.main_icon).click()

    def get_nav_element_visibility(self) -> bool:
        try:
            WebDriverWait(self.driver, 5).until(ec.visibility_of_element_located(BurgerMenu.nav_bar))
            return True
        except TimeoutException:
            return False

    def click_all_items_option(self):
        self.driver.find_element(*BurgerMenu.all_items).click()

    def click_about_option(self):
        self.driver.find_element(*BurgerMenu.about).click()

    def click_log_out_option(self):
        self.driver.find_element(*BurgerMenu.log_out).click()

    def click_reset_app_state_option(self):
        self.driver.find_element(*BurgerMenu.reset_app_state).click()

    def exit_menu(self):
        self.driver.find_element(*BurgerMenu.exit).click()