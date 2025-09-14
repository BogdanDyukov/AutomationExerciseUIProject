import allure
from playwright.sync_api import Page

from components.base_component import BaseComponent
from elements.clickable.button import Button
from elements.fields.input import Input
from elements.static.text import Text
from elements.static.title import Title


class LoginFormComponent(BaseComponent):
    def __init__(self, page: Page):
        super().__init__(page)

        self._title = Title(page, '//div[@class="login-form"]/h2', 'Login')

        self._email_input = Input(page, '//input[@data-qa="login-email"]', 'Email')
        self._password_input = Input(page, '//input[@data-qa="login-password"]', 'Password')

        self._login_button = Button(page, '//button[@data-qa="login-button"]', 'Login')

        self._incorrect_inputs_alert = Text(page, '//form[@action="/login"]/p', 'Incorrect Inputs')

    def check_title(self):
        expected_title = 'Login to your account'

        with allure.step(f'Check visible login form title with text "{expected_title}"'):
            self._title.check_visible()
            self._title.check_have_text(expected_title)

    @allure.step('Check visible login form fields')
    def check_fields(self, email: str = '', password: str = ''):
        self._email_input.check_visible()
        self._email_input.check_have_value(email)

        self._password_input.check_visible()
        self._password_input.check_have_value(password)

    def check_login_button(self):
        expected_text = 'Login'

        with allure.step(f'Check visible login button with text "{expected_text}"'):
            self._login_button.check_visible()
            self._login_button.check_have_text(expected_text)

    def check_incorrect_inputs_alert(self):
        expected_text = 'Your email or password is incorrect!'

        with allure.step(f'Check visible incorrect inputs alert with text "{expected_text}"'):
            self._incorrect_inputs_alert.check_visible()
            self._incorrect_inputs_alert.check_have_text(expected_text)

    @allure.step('Fill login form fields')
    def fill_fields(self, email: str, password: str):
        self._email_input.fill(email)
        self._password_input.fill(password)

    def click_login_button(self):
        self._login_button.click()
