from selenium.webdriver.common.by import By

from tests.conftest import URL


class Test1:

    def test_click_login_button(self, open_browser):
        driver = open_browser
        driver.find_element(By.ID, 'login-button').click()

        assert driver.current_url == URL, 'Aplicação não permaneceu na mesma página!'
        error_message = driver.find_element(By.CLASS_NAME, 'error-message-container').text
        assert error_message == 'Epic sadface: Username is required', 'Mensagem de erro inválida!'

