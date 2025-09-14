import re

import allure
from playwright.sync_api import Page, expect

from components.subscription.subscribe_to_updates_component import SubscribeToUpdatesComponent
from components.navigation.navbar_component import NavbarComponent
from config.routes import AppRoute


class BasePage:
    def __init__(self, page: Page, path: AppRoute):
        self._page = page
        self._path = path

        self.navbar_component: NavbarComponent = NavbarComponent(page)
        self.subscribe_to_updates_component: SubscribeToUpdatesComponent = SubscribeToUpdatesComponent(page)

    def open(self):
        with allure.step(f'Opening the url "{self._path}"'):
            self._page.goto(self._path)

    def is_open(self):
        with allure.step(f'Checking that page has a url "{self._path}"'):
            expect(self._page).to_have_url(re.compile(f".*{self._path}$"))
            self._page.wait_for_load_state()

    def reload(self):
        with allure.step(f'Reloading page with url "{self._page.url}"'):
            self._page.reload()

    def register_accept_dialog_handler(self):
        with allure.step('Registering the handler for the accept dialog'):
            self._page.once("dialog", lambda dialog: dialog.accept())

    def scroll_to_bottom(self):
        with allure.step('Scroll to the end of the page'):
            self._page.evaluate('window.scrollTo(0, document.body.scrollHeight)')
