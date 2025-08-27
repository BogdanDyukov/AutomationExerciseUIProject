from playwright.sync_api import expect

from elements.base_element import BaseElement


class CheckValueMixin:
    def check_have_value(self: BaseElement, value: str, nth: int = 0, **kwargs):
        locator = self.get_locator(nth, **kwargs)
        expect(locator).to_have_value(value)
