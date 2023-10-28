import time
from random import randint

from selenium.common import NoSuchElementException
from selenium.webdriver.common.by import By

from pages.PageObject import PageObject


class ProductsPage(PageObject):
    url = 'https://www.saucedemo.com/inventory.html'
    class_product_card = 'inventory_item'
    class_add_to_cart_btn = '.btn_primary'
    text_add_to_cart = 'Add to cart'
    class_remove_btn = 'btn_secondary'
    text_remove_btn = 'Remove'
    class_product_name = 'inventory_item_name'
    class_shopping_cart_badge = 'shopping_cart_badge'
    class_shopping_cart_link = 'shopping_cart_link'
    text_products_title = 'Products'

    def __init__(self, driver):
        super(ProductsPage, self).__init__(driver=driver)

    def is_url_products(self):
        return self.is_url(self.url)

    def has_title(self):
        return self.is_title(self.text_products_title)

    def has_menu_icon(self):
        try:
            menu = self.driver.find_element(By.ID, 'react-burger-menu-btn')
        except NoSuchElementException:
            return False
        return menu.is_displayed()

    def add_random_product_to_cart(self):
        products_list = self.driver.find_elements(By.CLASS_NAME, self.class_product_card)
        random_index = randint(0, len(products_list) - 1)
        product_card = products_list[random_index]
        add_to_cart_btn = product_card.find_element(By.CSS_SELECTOR, self.class_add_to_cart_btn)
        if add_to_cart_btn.text != self.text_add_to_cart:
            raise Exception('Add to cart button name is invalid!')
        add_to_cart_btn.click()
        remove_btn = product_card.find_element(By.CLASS_NAME, self.class_remove_btn)
        if remove_btn.text != self.text_remove_btn:
            raise Exception('Remove button name is invalid!')
        return product_card.find_element(By.CLASS_NAME, self.class_product_name).text

    def get_cart_number(self):
        return self.driver.find_element(By.CLASS_NAME, self.class_shopping_cart_badge).text

    def open_cart_page(self):
        self.driver.find_element(By.CLASS_NAME, self.class_shopping_cart_link).click()







