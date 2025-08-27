from playwright.sync_api import Page

from components.base_component import BaseComponent
from models.notification import Notification
from elements.clickable.button import Button
from elements.static.text import Text


class NotificationComponent(BaseComponent):
    def __init__(self, page: Page, identifier: str, data: Notification):
        super().__init__(page)

        self._data = data

        self._title = Text(page, f'//h2[@data-qa="account-{identifier}"]', 'Title')
        self._main_text = Text(page, '(//div[@class="col-sm-9 col-sm-offset-1"]/p)[1]', 'Main')
        self._additional_text = Text(page, '(//div[@class="col-sm-9 col-sm-offset-1"]/p)[2]', 'Additional')

        self._continue_button = Button(page, '//a[@data-qa="continue-button"]', 'Continue')

    def check_title(self):
        self._title.check_visible()
        self._title.check_have_text(self._data.title)

    def check_main_text(self):
        self._main_text.check_visible()
        self._main_text.check_have_text(self._data.main)

    def check_additional_text(self):
        self._additional_text.check_visible()
        self._additional_text.check_have_text(self._data.additional)

    def check_continue_button(self):
        self._continue_button.check_visible()
        self._continue_button.check_have_text('Continue')

    def check_all(self):
        self.check_title()
        self.check_main_text()
        self.check_additional_text()
        self.check_continue_button()

    def click_continue_button(self):
        self._continue_button.check_visible()
        self._continue_button.click()
