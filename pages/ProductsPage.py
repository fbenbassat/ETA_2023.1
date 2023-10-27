from selenium.common import NoSuchElementException
from selenium.webdriver.common.by import By

from pages.PageObject import PageObject


class ProductsPage(PageObject):
    url = 'https://www.saucedemo.com/inventory.html'

    def __init__(self, driver):
        super(ProductsPage, self).__init__(driver=driver)

    def is_url_products(self):
        return self.is_url(self.url)

    def has_title(self):
        title_text = self.driver.find_element(By.CLASS_NAME, 'title').text
        return title_text == 'Products'

    def has_menu_icon(self):
        try:
            menu = self.driver.find_element(By.ID, 'react-burger-menu-btn')
        except NoSuchElementException:
            return False
        return menu.is_displayed()
