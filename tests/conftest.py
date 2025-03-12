from selenium import webdriver
from pytest import fixture

from pages.login_page import LoginPage


@fixture(scope="session")
def driver():
    dr = webdriver.Chrome()
    yield dr
    dr.quit()

@fixture(scope="session")
def logged_in_driver(driver):
    lp = LoginPage(driver)
    lp.open()
    lp.login("standard_user", "secret_sauce")
    return driver