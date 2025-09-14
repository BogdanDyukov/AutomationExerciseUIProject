import allure
from playwright.sync_api import expect


class CheckableMixin:
    def set_checked(self, flag: bool, validate_check: bool = False, nth: int = 0, **kwargs):
        with allure.step(
                f'Set the {flag} flag for "{self._name}" {self._type_of} '
                f'{"with" if validate_check else "without"} validation'
        ):
            locator = self.get_locator(nth, **kwargs)
            locator.set_checked(flag)

            if validate_check:
                self.check_checked(flag, nth, **kwargs)

    def check_checked(self, flag: bool, nth: int = 0, **kwargs):
        with allure.step(f'Checking that "{self._name}" {self._type_of} has a flag "{flag}"'):
            locator = self.get_locator(nth, **kwargs)

            if flag:
                expect(locator).to_be_checked()
            else:
                expect(locator).not_to_be_checked()

