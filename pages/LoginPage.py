from selenium import webdriver
from selenium.webdriver.common.by import By

from pages.PageObject import PageObject


class LoginPage(PageObject):

    url = 'https://www.saucedemo.com/'

    def __init__(self):
        super(LoginPage, self).__init__()

    def open_page(self):
        self.driver.get(self.url)

    def click_login_btn(self):
        self.driver.find_element(By.ID, 'login-button').click()

    def is_url_login(self):
        return self.is_url(self.url)

    def has_login_error_message(self):
        error_message = self.driver.find_element(By.CLASS_NAME, 'error-message-container').text
        return error_message == 'Epic sadface: Username is required'

    def enter_login(self, user_name='standard_user', password='secret_sauce'):
        self.driver.find_element(By.ID, 'user-name').send_keys(user_name)
        self.driver.find_element(By.CSS_SELECTOR, '[data-test="password"]').send_keys(password)
        self.click_login_btn()

