from playwright.sync_api import Page

from components.base_component import BaseComponent
from elements.clickable.button import Button
from elements.fields.input import Input
from elements.static.text import Text
from elements.static.title import Title


class SignupFormComponent(BaseComponent):
    def __init__(self, page: Page):
        super().__init__(page)

        self._title = Title(page, '//div[@class="signup-form"]/h2', 'Title')

        self._name_input = Input(page, '//input[@data-qa="signup-name"]', 'Name')
        self._email_input = Input(page, '//input[@data-qa="signup-email"]', 'Email')

        self._signup_button = Button(page, '//button[@data-qa="signup-button"]', 'Signup')

        self._incorrect_inputs_alert = Text(page, '//form[@action="/signup"]/p', 'Incorrect Inputs')

    def check_title(self):
        self._title.check_visible()
        self._title.check_have_text('New User Signup!')

    def check_fields(self, name: str = '', email: str = ''):
        self._name_input.check_visible()
        self._name_input.check_have_value(name)

        self._email_input.check_visible()
        self._email_input.check_have_value(email)

    def check_signup_button(self):
        self._signup_button.check_visible()
        self._signup_button.check_have_text('Signup')

    def check_incorrect_inputs_alert(self):
        self._incorrect_inputs_alert.check_visible()
        self._incorrect_inputs_alert.check_have_text('Email Address already exist!')

    def check_all(
            self,
            name: str = '',
            email: str = '',
            incorrect_email_text_visible: bool = False):
        self.check_title()
        self.check_fields(name, email)

        if incorrect_email_text_visible:
            self.check_incorrect_inputs_alert()

        self.check_signup_button()

    def fill_fields(self, name: str, email: str):
        self._name_input.fill(name)
        self._email_input.fill(email)

    def click_signup_button(self):
        self._signup_button.click()
