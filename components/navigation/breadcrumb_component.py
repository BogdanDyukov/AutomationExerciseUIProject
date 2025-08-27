from playwright.sync_api import Page

from components.base_component import BaseComponent
from elements.clickable.link import Link
from elements.static.text import Text


class BreadcrumbComponent(BaseComponent):
    def __init__(self, page: Page, root_link_name: str):
        super().__init__(page)

        self._root_link_name = root_link_name

        self._current_page_item = Text(page, '//li[@class="active"]', 'Current Page Item')

        self._root_link = Link(page, f'//a[text()="{root_link_name}"]', 'Root')

    def check_breadcrumb_current_item(self, current_page_item: str):
        self._current_page_item.check_visible()
        self._current_page_item.check_have_text(current_page_item)

    def check_breadcrumb_home_item_link(self):
        self._root_link.check_visible()
        self._root_link.check_have_text(self._root_link_name)

    def check_all(self, current_page_item: str):
        self.check_breadcrumb_current_item(current_page_item)
        self.check_breadcrumb_home_item_link()

    def click_breadcrumb_home_item_link(self):
        self._root_link.check_visible()
        self._root_link.click()
