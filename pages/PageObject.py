from selenium import webdriver


class PageObject:

    def __init__(self, driver=None):
        if driver:
            self.driver = driver
        else:
            self.driver = webdriver.Chrome()

    def is_url(self, url):
        return self.driver.current_url == url

    def close(self):
        self.driver.quit()
