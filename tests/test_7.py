import time

from pages.ProductsPage import ProductsPage


class Test7:

    def test_order_products_low_to_high(self, login_saucedemo):
        products_p = ProductsPage(driver=login_saucedemo.driver)
        assert products_p.is_url_products(), 'Products page not found!'
        products_p.order_products_by_price_low_to_high()
        assert products_p.check_order_price_low_to_high(), 'Order price not correct!'



