from playwright.sync_api import expect


class FillableMixin:
    def fill(self, value: str, validate_value: bool = False, nth: int = 0, **kwargs):
        locator = self.get_locator(nth, **kwargs)
        locator.fill(value)

        if validate_value:
            self.check_have_value(value, nth, **kwargs)

    def check_have_value(self, value: str, nth: int = 0, **kwargs):
        locator = self.get_locator(nth, **kwargs)
        expect(locator).to_have_value(value)
