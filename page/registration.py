from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By


class RegistrationPage:

    URL = 'https://ru.rsdelivers.com/Register/Register'

    def __init__(self, browsers):
        self.browsers = browsers

    def load_page(self):
        self.browsers.get(self.URL)


class RegistrationFieldLogin(RegistrationPage):

    INPUT_LOGIN = (By.ID, 'txtUserName')
    ERROR_LOGIN = (By.CSS_SELECTOR, '#errorUsername')

    def input_login(self, login):
        login_input = self.browsers.find_element(*self.INPUT_LOGIN)
        login_input.send_keys(login + Keys.RETURN)

    def error_login_text(self):
        error_login = self.browsers.find_element(*self.ERROR_LOGIN)
        return error_login.text

    def field_login_value(self):
        login_value = self.browsers.find_element(*self.INPUT_LOGIN)
        return login_value.get_attribute('value')