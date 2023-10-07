from selenium.common import NoSuchElementException
from selenium.webdriver.common.by import By


class ProductsPage:
    url = 'https://www.saucedemo.com/inventory.html'

    def __init__(self, driver):
        self.driver = driver

    def is_url(self):
        return self.driver.current_url == self.url

    def has_title(self):
        title_text = self.driver.find_element(By.CLASS_NAME, 'title').text
        return title_text == 'Products'

    def has_menu_icon(self):
        try:
            menu = self.driver.find_element(By.ID, 'react-burger-menu-btn')
        except NoSuchElementException:
            return False
        return menu.is_displayed()
