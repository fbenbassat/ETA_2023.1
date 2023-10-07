from selenium import webdriver
from selenium.webdriver.common.by import By


class LoginPage:

    url = 'https://www.saucedemo.com/'

    def __init__(self):
        self.driver = webdriver.Chrome()

    def open_page(self):
        self.driver.get(self.url)

    def click_login_btn(self):
        self.driver.find_element(By.ID, 'login-button').click()

    def is_url(self):
        return self.driver.current_url == self.url

    def has_login_error_message(self):
        error_message = self.driver.find_element(By.CLASS_NAME, 'error-message-container').text
        return error_message == 'Epic sadface: Username is required'

    def enter_login(self, user_name='standard_user', password='secret_sauce'):
        self.driver.find_element(By.ID, 'user-name').send_keys(user_name)
        self.driver.find_element(By.CSS_SELECTOR, '[data-test="password"]').send_keys(password)
        self.click_login_btn()

    def close(self):
        self.driver.quit()

