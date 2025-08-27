from playwright.sync_api import expect

from elements.base_element import BaseElement


class CheckableMixin:
    def set_checked(self: BaseElement, flag: bool, nth: int = 0, **kwargs):
        locator = self.get_locator(nth, **kwargs)
        locator.set_checked(flag)

    def check_checked(self: BaseElement, flag: bool, nth: int = 0, **kwargs):
        locator = self.get_locator(nth, **kwargs)

        if flag:
            expect(locator).to_be_checked()
        else:
            expect(locator).not_to_be_checked()

