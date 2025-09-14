import re

import allure
from playwright.sync_api import expect

from pages.base.base_page import BasePage


class BaseDynamicPage(BasePage):
    def open(self, **kwargs):
        path = self._path.format(**kwargs)

        with allure.step(f'Opening the url "{path}"'):
            self._page.goto(path)

    def is_open(self, **kwargs):
        path = self._path.format(**kwargs)

        with allure.step(f'Checking that page has a url "{path}"'):
            expect(self._page).to_have_url(re.compile(f".*{path}$"))
            self._page.wait_for_load_state()
