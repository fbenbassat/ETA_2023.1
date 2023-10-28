from pages.ProductsPage import ProductsPage
from pages.YourCartPage import YourCartPage


class Test4:

    def test_add_product_to_cart(self, login_saucedemo):
        products_p = ProductsPage(login_saucedemo.driver)
        product_name = products_p.add_random_product_to_cart()
        assert products_p.get_cart_number() == '1', 'Não foi encontrado o numero 1 no carrinho.'
        products_p.open_cart_page()
        your_cart_p = YourCartPage(driver=products_p.driver)
        assert your_cart_p.is_your_cart_page(), 'Your Cart page not found!'
        assert your_cart_p.get_first_product_item_list() == product_name, 'Nome do produto inválido!'



