from playwright.sync_api import Page

from components.navigation.navbar_component import NavbarComponent
from components.interactions.subscribe_to_updates_component import SubscribeToUpdatesComponent
from elements.static.text import Text
from pages.base.base_page import BasePage
from config.routes import AppRoute


class TestCasesPage(BasePage):
    __test__ = False  # pytest перестанет воспринимать это как тестовый класс

    def __init__(self, page: Page, path: AppRoute):
        super().__init__(page, path)

        self.navbar_component: NavbarComponent = NavbarComponent(page)
        self.subscribe_to_updates_component: SubscribeToUpdatesComponent = SubscribeToUpdatesComponent(page)

        self._title = Text(page, '//h2[contains(., "Test Cases")]', 'Title')
        self._description_text = Text(page, '//span[contains(text(), "Below is the")]', 'Description')

    def check_title(self):
        self._title.check_visible()
        self._title.check_have_text('Test Cases')

    def check_description_text(self):
        self._description_text.check_visible()
        self._description_text.check_have_text(
            'Below is the list of test Cases for you to practice the '
            'Automation. Click on the scenario for detailed Test Steps:'
        )
