import time

from selenium.common import NoSuchElementException, TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from pages.PageObject import PageObject


class MenuPage(PageObject):

    id_menu_btn = 'react-burger-menu-btn'
    id_close_btn = 'react-burger-cross-btn'
    id_logout_btn = 'logout_sidebar_link'

    def __init__(self, driver):
        super(MenuPage, self).__init__(driver=driver)

    def open_menu(self):
        self.driver.find_element(By.ID, self.id_menu_btn).click()

    def is_menu_open(self):
        return self.wait_visible_element(By.ID, self.id_close_btn, 4)

    def click_logout(self):
        self.driver.find_element(By.ID, self.id_logout_btn).click()
