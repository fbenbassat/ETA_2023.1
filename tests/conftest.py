import pytest

from pages.LoginPage import LoginPage
from pages.ProductsPage import ProductsPage


def pytest_addoption(parser):
    parser.addoption("--browser_selenium", default='chrome', help='Select browser')


@pytest.fixture()
def open_browser(request):
    select_browser = request.config.getoption("--browser_selenium").lower()
    if select_browser not in ['chrome', 'safari', 'firefox']:
        raise Exception('Browser not supported')
    login_p = LoginPage(browser=select_browser)
    login_p.open_page()
    yield login_p
    login_p.close()


@pytest.fixture()
def run_all_browser(all_browsers):
    login_p = LoginPage(browser=all_browsers)
    login_p.open_page()
    yield login_p
    login_p.close()


@pytest.fixture()
def login_saucedemo(open_browser):
    login_p = open_browser
    login_p.enter_login()
    yield login_p


@pytest.fixture()
def add_product_to_cart(login_saucedemo):
    products_p = ProductsPage(login_saucedemo.driver)
    products_p.add_random_product_to_cart()
    yield products_p




