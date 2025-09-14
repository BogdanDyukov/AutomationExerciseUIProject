import allure
from playwright.sync_api import Page

from components.base_component import BaseComponent
from elements.clickable.link import Link
from elements.static.text import Text
from models.breadcrumb import Breadcrumb


class BreadcrumbComponent(BaseComponent):
    def __init__(self, page: Page, identifier: str, data: Breadcrumb):
        super().__init__(page)

        self._data = data

        self._current_page_item = Text(page, '//li[@class="active"]', 'Current Page Item')

        self._root_link = Link(page, f'//a[text()="{identifier}"]', 'Root')

    def check_breadcrumb_current_item(self):
        expected_text = self._data.current_page_item_text
        with allure.step(f'Check visible breadcrumb current item with text "{expected_text}"'):
            self._current_page_item.check_visible()
            self._current_page_item.check_have_text(expected_text)

    def check_breadcrumb_home_item_link(self):
        expected_text = self._data.root_link_name_text
        with allure.step(f'Check visible breadcrumb home item link with text "{expected_text}"'):
            self._root_link.check_visible()
            self._root_link.check_have_text(expected_text)

    def click_breadcrumb_home_item_link(self):
        self._root_link.click()
