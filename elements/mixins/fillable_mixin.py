import allure
from playwright.sync_api import expect


class FillableMixin:
    def fill(self, value: str, validate_value: bool = False, nth: int = 0, **kwargs):
        with allure.step(
                f'Fill "{self._name}" {self._type_of} to value "{value}" '
                f'{"with" if validate_value else "without"} validation'
        ):
            locator = self.get_locator(nth, **kwargs)
            locator.fill(value)

        if validate_value:
            self.check_have_value(value, nth, **kwargs)

    def check_have_value(self, value: str, nth: int = 0, **kwargs):
        with allure.step(f'Checking that "{self._name}" {self._type_of} has a value "{value}"'):
            locator = self.get_locator(nth, **kwargs)
            expect(locator).to_have_value(value)
