import allure
from playwright.sync_api import Page

from components.base_component import BaseComponent
from elements.clickable.button import Button
from elements.fields.input import Input
from elements.static.text import Text
from elements.static.title import Title


class SubscribeToUpdatesComponent(BaseComponent):
    def __init__(self, page: Page):
        super().__init__(page)

        self._title = Title(page, '//h2[text()="Subscription"]', 'Subscription')
        self._note_text = Text(page, '//p[contains(text(), "Get the most")]', 'Note')

        self._email_input = Input(page, '//input[@id="susbscribe_email"]', 'Email')

        self._subscribe_button = Button(page, '//button[@id="subscribe"]', 'Subscribe')

        self._success_subscribe_alert = Text(
            page, '//div[contains(text(), "You have been")]', 'Success Subscribe'
        )

    def check_title(self):
        expected_text = 'Subscription'

        with allure.step(f'Check visible subscribe to updates title with text "{expected_text}"'):
            self._title.check_visible()
            self._title.check_have_text(expected_text)

    def check_note_text(self):
        expected_text = 'Get the most recent updates from our site and be updated your self...'

        with allure.step(f'Check visible subscribe to updates note text "{expected_text}"'):
            self._note_text.check_visible()
            self._note_text.check_have_text(expected_text)

    @allure.step('Check visible subscribe to updates fields')
    def check_fields(self, email: str = ''):
        self._email_input.check_visible()
        self._email_input.check_have_value(email)

    def check_subscribe_button(self):
        self._subscribe_button.check_visible()

    def check_success_subscribe_alert(self):
        expected_text = 'You have been successfully subscribed!'

        with allure.step(f'Check visible subscribe to updates success alert with text "{expected_text}"'):
            self._success_subscribe_alert.check_visible()
            self._success_subscribe_alert.check_have_text(expected_text)

    @allure.step('Fill subscribe to updates fields')
    def fill_fields(self, email: str):
        self._email_input.fill(email)

    def click_subscribe_button(self):
        self._subscribe_button.click()
