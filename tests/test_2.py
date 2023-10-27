import pytest

from pages.ProductsPage import ProductsPage


class Test2:

    def test_login_saucedemo(self, open_browser):
        login_p = open_browser
        login_p.enter_login()
        products_p = ProductsPage(driver=login_p.driver)
        assert products_p.is_url_products(), 'URL da página de produtos inválida!'
        assert products_p.has_title(), 'Título da página de produtos inválido!'
        assert products_p.has_menu_icon(), 'Menu não encontrado!'


