from playwright.sync_api import Page

from components.base_component import BaseComponent
from elements.clickable.button import Button
from elements.fields.input import Input


class SearchFieldComponent(BaseComponent):
    def __init__(self, page: Page):
        super().__init__(page)

        self._search_input = Input(page, '//input[@id="search_product"]', 'Search')
        self._submit_button = Button(page, '//button[@id="submit_search"]', 'Submit')

    def check_fields(self, search_query: str = ''):
        self._search_input.check_visible()
        self._search_input.check_have_value(search_query)

    def check_submit_button(self):
        self._submit_button.check_visible()

    def check_all(self, search_query: str = ''):
        self.check_fields(search_query)
        self.check_submit_button()

    def fill_fields(self, search_query: str):
        self._search_input.fill(search_query)

    def click_submit_button(self):
        self._submit_button.click()
