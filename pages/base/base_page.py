import re

from playwright.sync_api import Page, expect

from config.routes import AppRoute


class BasePage:
    def __init__(self, page: Page, path: AppRoute):
        self._page = page
        self._path = path

    def open(self):
        self._page.goto(self._path)

    def is_open(self):
        expect(self._page).to_have_url(re.compile(f".*{self._path}$"))
        self._page.wait_for_load_state()

    def reload(self):
        self._page.reload()

    def register_accept_dialog_handler(self):
        self._page.once("dialog", lambda dialog: dialog.accept())
