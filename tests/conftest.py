from selenium import webdriver
from pytest import fixture

from pages.login_page import LoginPage
from utils.credentials import Credentials


def pytest_addoption(parser):
    """Adds command-line options for pytest."""
    parser.addoption("--user",
                     action="store",
                     default="standard",
                     help="User to login and perform tests with")

@fixture(scope="session")
def user(request):
    """Returns the user specified by the --user command-line option."""
    return request.config.getoption("--user")

@fixture(scope="session")
def driver():
    """Provides a WebDriver instance for the test session."""
    dr = webdriver.Chrome()
    yield dr
    dr.quit()

@fixture(scope="session")
def logged_in_driver(driver, user):
    """Provides a logged-in WebDriver instance for the test session."""
    lp = LoginPage(driver)
    lp.open()
    us = Credentials(user)
    lp.login(us.username, us.password)
    if lp.is_login_successful():
        return driver
    else:
        raise Exception(f"Login failed for user: {user}")
