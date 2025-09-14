import allure
from playwright.sync_api import Page

from components.base_component import BaseComponent
from elements.clickable.button import Button
from elements.fields.input import Input
from elements.static.text import Text
from elements.static.title import Title


class SignupFormComponent(BaseComponent):
    def __init__(self, page: Page):
        super().__init__(page)

        self._title = Title(page, '//div[@class="signup-form"]/h2', 'Signup')

        self._name_input = Input(page, '//input[@data-qa="signup-name"]', 'Name')
        self._email_input = Input(page, '//input[@data-qa="signup-email"]', 'Email')

        self._signup_button = Button(page, '//button[@data-qa="signup-button"]', 'Signup')

        self._incorrect_inputs_alert = Text(page, '//form[@action="/signup"]/p', 'Incorrect Inputs')

    def check_title(self):
        expected_title = 'New User Signup!'

        with allure.step(f'Check visible signup form title with text"{expected_title}"'):
            self._title.check_visible()
            self._title.check_have_text(expected_title)

    @allure.step('Check visible signup form fields')
    def check_fields(self, name: str = '', email: str = ''):
        self._name_input.check_visible()
        self._name_input.check_have_value(name)

        self._email_input.check_visible()
        self._email_input.check_have_value(email)

    def check_signup_button(self):
        expected_text = 'Signup'

        with allure.step(f'Check visible signup form button with text "{expected_text}"'):
            self._signup_button.check_visible()
            self._signup_button.check_have_text(expected_text)

    def check_incorrect_inputs_alert(self):
        expected_text = 'Email Address already exist!'

        with allure.step(f'Check visible signup form incorrect inputs alert with text "{expected_text}"'):
            self._incorrect_inputs_alert.check_visible()
            self._incorrect_inputs_alert.check_have_text(expected_text)

    @allure.step('Fill signup form fields')
    def fill_fields(self, name: str, email: str):
        self._name_input.fill(name)
        self._email_input.fill(email)

    def click_signup_button(self):
        self._signup_button.click()
