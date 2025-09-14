import allure
from playwright.sync_api import expect


class DisableableMixin:
    def check_enabled(self, nth: int = 0, **kwargs):
        with allure.step(f'Checking that "{self._name}" {self._type_of} is enable'):
            locator = self.get_locator(nth, **kwargs)
            expect(locator).to_be_enabled()

    def check_disabled(self, nth: int = 0, **kwargs):
        with allure.step(f'Checking that "{self._name}" {self._type_of} is disable'):
            locator = self.get_locator(nth, **kwargs)
            expect(locator).to_be_disabled()
