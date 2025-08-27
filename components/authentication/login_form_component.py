from playwright.sync_api import Page

from components.base_component import BaseComponent
from elements.clickable.button import Button
from elements.fields.input import Input
from elements.static.text import Text


class LoginFormComponent(BaseComponent):
    def __init__(self, page: Page):
        super().__init__(page)

        self._title = Text(page, '//div[@class="login-form"]/h2', 'Title')

        self._email_input = Input(page, '//input[@data-qa="login-email"]', 'Email')
        self._password_input = Input(page, '//input[@data-qa="login-password"]', 'Password')

        self._login_button = Button(page, '//button[@data-qa="login-button"]', 'Login')

        self._incorrect_inputs_alert = Text(page, '//form[@action="/login"]/p', 'Incorrect Inputs')

    def check_title(self):
        self._title.check_visible()
        self._title.check_have_text('Login to your account')

    def check_fields(self, email: str = '', password: str = ''):
        self._email_input.check_visible()
        self._email_input.check_have_value(email)

        self._password_input.check_visible()
        self._password_input.check_have_value(password)

    def check_login_button(self):
        self._login_button.check_visible()
        self._login_button.check_have_text('Login')

    def check_incorrect_inputs_text(self):
        self._incorrect_inputs_alert.check_visible()
        self._incorrect_inputs_alert.check_have_text('Your email or password is incorrect!')

    def check_all(
            self,
            email: str = '',
            password: str = '',
            incorrect_email_or_password_text_visible: bool = False):
        self.check_title()
        self.check_fields(email, password)

        if incorrect_email_or_password_text_visible:
            self.check_incorrect_inputs_text()

        self.check_login_button()

    def fill_fields(self, email: str, password: str):
        self._email_input.check_visible()
        self._email_input.fill(email)
        self._email_input.check_have_value(email)

        self._email_input.check_visible()
        self._password_input.fill(password)
        self._password_input.check_have_value(password)

    def click_login_button(self):
        self._login_button.check_visible()
        self._login_button.click()
