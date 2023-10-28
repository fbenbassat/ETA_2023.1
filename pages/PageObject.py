from selenium import webdriver
from selenium.common import TimeoutException
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


class PageObject:

    def __init__(self, driver=None):
        if driver:
            self.driver = driver
        else:
            self.driver = webdriver.Chrome()

    def is_url(self, url):
        return self.driver.current_url == url

    def wait_visible_element(self, by, value, timeout):
        try:
            element = WebDriverWait(self.driver, timeout).until(
                expected_conditions.visibility_of_element_located((by, value)))
        except TimeoutException:
            return False
        return element.is_displayed()

    def close(self):
        self.driver.quit()
