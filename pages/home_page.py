from playwright.sync_api import Page

from components.navigation.navbar_component import NavbarComponent
from components.interactions.subscribe_to_updates_component import SubscribeToUpdatesComponent
from pages.base.base_page import BasePage
from config.routes import AppRoute


class HomePage(BasePage):
    def __init__(self, page: Page, path: AppRoute):
        super().__init__(page, path)

        self.navbar_component: NavbarComponent = NavbarComponent(page)
        self.subscribe_to_updates_component: SubscribeToUpdatesComponent = SubscribeToUpdatesComponent(page)
