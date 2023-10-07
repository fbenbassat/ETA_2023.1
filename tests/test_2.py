import time

import pytest
from selenium import webdriver
from selenium.common import NoSuchElementException
from selenium.webdriver.common.by import By


class Test2:

    def test_login_saucedemo(self, open_browser):
        driver = open_browser.driver
        driver.find_element(By.ID, 'user-name').send_keys('standard_user')
        driver.find_element(By.CSS_SELECTOR, '[data-test="password"]').send_keys('secret_sauce')
        driver.find_element(By.ID, 'login-button').click()

        assert driver.current_url == 'https://www.saucedemo.com/inventory.html', 'URL da página de produtos inválida!'

        title_text = driver.find_element(By.CLASS_NAME, 'title').text
        assert title_text == 'Products', 'Título da página de produtos inválido!'

        try:
            menu = driver.find_element(By.ID, 'react-burger-menu-btn')
        except NoSuchElementException:
            pytest.fail('Elemento Menu não encontrado!')
        assert menu.is_displayed(), 'Menu não encontrado!'


