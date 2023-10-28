from selenium.webdriver.common.by import By

from pages.PageObject import PageObject


class YourCartPage(PageObject):
    url = 'https://www.saucedemo.com/cart.html'
    title_your_cart = 'Your Cart'
    class_product_name = 'inventory_item_name'
    xpath_checkout_btn = '//*[@id="checkout"]'

    def __init__(self, driver):
        super(YourCartPage, self).__init__(driver=driver)

    def is_your_cart_page(self):
        return self.is_page(self.url, self.title_your_cart)

    def get_first_product_item_list(self):
        return self.driver.find_element(By.CLASS_NAME, self.class_product_name).text

    def click_checkout(self):
        self.driver.find_element(By.XPATH, self.xpath_checkout_btn).click()
