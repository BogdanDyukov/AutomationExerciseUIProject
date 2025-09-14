import allure
from playwright.sync_api import Page

from components.navigation.navbar_component import NavbarComponent
from components.subscription.subscribe_to_updates_component import SubscribeToUpdatesComponent
from elements.static.text import Text
from elements.static.title import Title
from pages.base.base_page import BasePage
from config.routes import AppRoute


class TestCasesPage(BasePage):
    __test__ = False  # pytest перестанет воспринимать это как тестовый класс

    def __init__(self, page: Page, path: AppRoute):
        super().__init__(page, path)

        self.navbar_component: NavbarComponent = NavbarComponent(page)
        self.subscribe_to_updates_component: SubscribeToUpdatesComponent = SubscribeToUpdatesComponent(page)

        self._title = Title(page, '//h2[contains(., "Test Cases")]', 'Test Cases')
        self._description_text = Text(page, '//span[contains(text(), "Below is the")]', 'Description')

    def check_title(self):
        expected_text = 'Test Cases'
        with allure.step(f'Check visible title with text "{expected_text}"'):
            self._title.check_visible()
            self._title.check_have_text(expected_text)

    def check_description_text(self):
        expected_text = (
            'Below is the list of test Cases for you to practice the '
            'Automation. Click on the scenario for detailed Test Steps:'
        )
        with allure.step(f'Check visible description text "{expected_text}"'):
            self._description_text.check_visible()
            self._description_text.check_have_text(expected_text)
