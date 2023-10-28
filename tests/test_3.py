import time

from pages.LoginPage import LoginPage
from pages.MenuPage import MenuPage


class Test3:

    def test_logout(self, login_saucedemo):
        login_p = login_saucedemo
        menu_p = MenuPage(driver=login_p.driver)
        menu_p.open_menu()
        assert menu_p.is_menu_open(), 'Menu is not open!'
        menu_p.click_logout()
        assert login_p.is_url_login(), 'URL de login não encontrado!'
