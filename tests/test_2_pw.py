import time

from playwright.sync_api import Page, expect

class Test2_pw:

    def test_2_pw(self, page: Page):

        page.goto('https://www.saucedemo.com/')

        expect(page).to_have_title('Swag Labs')

        page.locator('#user-name').fill('standard_user')
        page.locator('#password').fill('secret_sauce')

        page.locator('[name="login-button"]').click()

        expect(page).to_have_url('https://www.saucedemo.com/inventory.html')
        expect(page.locator('.title')).to_have_text('Products2')

