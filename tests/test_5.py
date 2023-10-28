
from pages.YourCartPage import YourCartPage
from pages.YourInfoCheckoutPage import YourInfoCheckoutPage


class Test5:

    def test_checkout_message_error(self, add_product_to_cart):
        products_p = add_product_to_cart
        products_p.open_cart_page()
        your_cart_p = YourCartPage(products_p.driver)
        your_cart_p.click_checkout()
        your_info_checkout_p = YourInfoCheckoutPage(driver=your_cart_p.driver)
        assert your_info_checkout_p.is_your_info_checkout_page(), 'Checkout: Your Information page not found!'
        your_info_checkout_p.click_continue()
        assert your_info_checkout_p.is_your_info_checkout_page(), 'Após click continue a aplicação mudou de página!'
        assert your_info_checkout_p.has_error_message(), 'Messagem de erro não encontrada!'


