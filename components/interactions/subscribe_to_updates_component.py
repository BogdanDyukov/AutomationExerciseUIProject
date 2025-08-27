from playwright.sync_api import Page

from components.base_component import BaseComponent
from elements.clickable.button import Button
from elements.fields.input import Input
from elements.static.text import Text


class SubscribeToUpdatesComponent(BaseComponent):
    def __init__(self, page: Page):
        super().__init__(page)

        self._title = Text(page, '//h2[text()="Subscription"]', 'Title')
        self._note_text = Text(page, '//p[contains(text(), "Get the most")]', 'Note')

        self._email_input = Input(page, '//input[@id="susbscribe_email"]', 'Email')

        self._subscribe_button = Button(page, '//button[@id="subscribe"]', 'Subscribe')

        self._success_subscribe_alert = Text(
            page, '//div[contains(text(), "You have been")]', 'Success Subscribe'
        )

    def check_title(self):
        self._title.check_visible()
        self._title.check_have_text('Subscription')

    def check_note_text(self):
        self._note_text.check_visible()
        self._note_text.check_have_text('Get the most recent updates from our site and be updated your self...')

    def check_fields(self, email: str = ''):
        self._email_input.check_visible()
        self._email_input.check_have_value(email)

    def check_subscribe_button(self):
        self._subscribe_button.check_visible()

    def check_success_subscribe_alert(self):
        self._success_subscribe_alert.check_visible()
        self._success_subscribe_alert.check_have_text('You have been successfully subscribed!')

    def check_all(self, email: str = '', is_subscription_completed: bool = False):

        if is_subscription_completed:
            self.check_success_subscribe_alert()

        self.check_title()
        self.check_fields(email)
        self.check_subscribe_button()
        self.check_note_text()

    def fill_fields(self, email: str):
        self._email_input.check_visible()
        self._email_input.fill(email)
        self._email_input.check_have_value(email)

    def click_subscribe_button(self):
        self._subscribe_button.check_visible()
        self._subscribe_button.click()
