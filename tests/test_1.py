import pytest


class Test1:

    @pytest.mark.parametrize('all_browsers', ['chrome', 'safari', 'firefox'])
    def test_click_login_button(self, run_all_browser):
        login_p = run_all_browser
        login_p.click_login_btn()
        assert login_p.is_url_login(), 'Aplicação não permaneceu na mesma página!'
        assert login_p.has_login_error_message(), 'Mensagem de erro inválida!'

