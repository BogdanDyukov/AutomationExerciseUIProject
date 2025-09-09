from playwright.sync_api import Page

from components.base_component import BaseComponent
from elements.clickable.button import Button
from elements.clickable.link import Link
from elements.static.subtitle import Subtitle
from elements.static.text import Text
from models.modal_dialog import ModalDialog


class ModalDialogComponent(BaseComponent):
    def __init__(self, page: Page, identifier: str, data: ModalDialog):
        super().__init__(page)

        self._data = data

        self._title = Subtitle(page, f'//div[@id="{identifier}"]//h4', 'Title')
        self._note_text = Text(page, f'(//div[@id="{identifier}"]//p)[1]', 'Note')

        self._navigation_link = Link(page, f'//div[@id="{identifier}"]//a', 'Navigation')
        self._continue_button = Button(page, f'//div[@id="{identifier}"]//button', 'Continue')

    def check_title(self):
        self._title.check_visible()
        self._title.check_have_text(self._data.title)

    def check_note_text(self):
        self._note_text.check_visible()
        self._note_text.check_have_text(self._data.note_text)

    def check_navigation_link(self):
        self._navigation_link.check_visible()
        self._navigation_link.check_have_text(self._data.navigation_link_text)

    def check_continue_button(self):
        self._continue_button.check_visible()
        self._continue_button.check_have_text(self._data.continue_button_text)

    def check_all(self):
        self.check_title()
        self.check_note_text()
        self.check_navigation_link()
        self.check_continue_button()

    def click_navigation_link(self):
        self._navigation_link.click()

    def click_continue_button(self):
        self._continue_button.click()

