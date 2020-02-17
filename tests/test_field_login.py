import pytest
from page.registration import RegistrationFieldLogin
from generator.login_data import GeneratorLogin
import string

Data = GeneratorLogin(string)
Data.data_login()


@pytest.mark.parametrize("LOGIN, ERROR_LOGIN", Data.data_login())

def test_user_field(browser, LOGIN, ERROR_LOGIN):
    registration_page = RegistrationFieldLogin(browser)
    registration_page.load_page()
    registration_page.input_login(LOGIN)

    assert registration_page.error_login_text() == ERROR_LOGIN

    if len(LOGIN) > 64:
        LOGIN_RES = LOGIN[0:64]
        assert registration_page.field_login_value() == LOGIN_RES
    elif len(LOGIN) <= 64:
        assert registration_page.field_login_value() == LOGIN
