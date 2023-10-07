import pytest

from pages.LoginPage import LoginPage


@pytest.fixture
def open_browser():
    login_p = LoginPage()
    login_p.open_page()
    yield login_p
    login_p.close()
