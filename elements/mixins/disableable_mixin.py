from playwright.sync_api import expect

from elements.base_element import BaseElement


class DisableableMixin:
    def check_enabled(self: BaseElement, nth: int = 0, **kwargs):
        locator = self.get_locator(nth, **kwargs)
        expect(locator).to_be_enabled()

    def check_disabled(self: BaseElement, nth: int = 0, **kwargs):
        locator = self.get_locator(nth, **kwargs)
        expect(locator).to_be_disabled()
