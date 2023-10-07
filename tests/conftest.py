import pytest
from selenium import webdriver

URL = 'https://www.saucedemo.com/'


@pytest.fixture
def open_browser():
    driver = webdriver.Chrome()
    driver.get(URL)
    yield driver
    driver.quit()
