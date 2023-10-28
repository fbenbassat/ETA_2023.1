from selenium.webdriver.common.by import By

from pages.PageObject import PageObject


class YourInfoCheckoutPage(PageObject):

    url = 'https://www.saucedemo.com/checkout-step-one.html'
    text_page_title = 'Checkout: Your Information'
    css_continue_btn = '[data-test="continue"]'
    text_error_message = 'Error: First Name is required'
    css_error_message = '.error-message-container'

    def __init__(self, driver):
        super(YourInfoCheckoutPage, self).__init__(driver=driver)

    def is_your_info_checkout_page(self):
        return self.is_page(self.url, self.text_page_title)

    def click_continue(self):
        self.driver.find_element(By.CSS_SELECTOR, self.css_continue_btn).click()

    def has_error_message(self):
        return self.driver.find_element(By.CSS_SELECTOR, self.css_error_message).text == self.text_error_message



