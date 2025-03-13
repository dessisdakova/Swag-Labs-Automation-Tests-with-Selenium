from selenium import webdriver
from pytest import fixture

from pages.login_page import LoginPage
from tests.credentials import Credentials


def pytest_addoption(parser):
    parser.addoption("--user",
                     action="store",
                     help="User to login and perform tests with")

@fixture(scope="session")
def user(request):
    return request.config.getoption("--user")

@fixture(scope="session")
def driver():
    dr = webdriver.Chrome()
    yield dr
    dr.quit()

@fixture(scope="session")
def logged_in_driver(driver, user):
    lp = LoginPage(driver)
    lp.open()
    us = Credentials(user)
    lp.login(us.username, us.password)
    return driver