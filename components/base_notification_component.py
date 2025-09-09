from playwright.async_api import Page

from components.base_component import BaseComponent
from elements.clickable.button import Button
from elements.static.text import Text
from elements.static.title import Title
from models.notification import Notification


class BaseNotificationComponent(BaseComponent):
    def __init__(self, page: Page, identifier: str, data: Notification):
        super().__init__(page)

        self._data = data

        self._title = Title(page, f'//h2[@data-qa="{identifier}"]', 'Title')
        self._main_text = Text(page, '(//div[@class="col-sm-9 col-sm-offset-1"]/p)[1]', 'Main')

        self._continue_button = Button(page, '//a[@data-qa="continue-button"]', 'Continue')

    def check_title(self):
        self._title.check_visible()
        self._title.check_have_text(self._data.title)

    def check_main_text(self):
        self._main_text.check_visible()
        self._main_text.check_have_text(self._data.main_text)

    def check_continue_button(self):
        self._continue_button.check_visible()
        self._continue_button.check_have_text('Continue')

    def _check_all(self):
        self.check_title()
        self.check_main_text()
        self.check_continue_button()

    def click_continue_button(self):
        self._continue_button.click()
