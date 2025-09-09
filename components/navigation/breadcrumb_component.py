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
        self._current_page_item.check_visible()
        self._current_page_item.check_have_text(self._data.current_page_item_text)

    def check_breadcrumb_home_item_link(self):
        self._root_link.check_visible()
        self._root_link.check_have_text(self._data.root_link_name_text)

    def check_all(self):
        self.check_breadcrumb_current_item()
        self.check_breadcrumb_home_item_link()

    def click_breadcrumb_home_item_link(self):
        self._root_link.click()
