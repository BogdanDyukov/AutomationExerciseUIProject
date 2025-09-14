import allure
from playwright.sync_api import Page, Locator, expect


class BaseElement:
    def __init__(self, page: Page, locator: str, name: str):
        self._page = page
        self._locator = locator
        self._name = name

    @property
    def _type_of(self) -> str:
        return "base element"

    def get_locator(self, nth: int = 0, **kwargs) -> Locator:
        locator = self._locator.format(**kwargs)

        with allure.step(f'Getting locator with "xpath={locator}" at index "{nth}"'):
            return self._page.locator(locator).nth(nth)

    def check_visible(self, nth: int = 0, **kwargs):
        with allure.step(f'Checking that "{self._name}" {self._type_of} is visible'):
            locator = self.get_locator(nth, **kwargs)
            expect(locator).to_be_visible()

    def check_have_text(self, text: str, nth: int = 0, **kwargs):
        with allure.step(f'Checking that "{self._name}" {self._type_of} has text "{text}"'):
            locator = self.get_locator(nth, **kwargs)
            expect(locator).to_have_text(text)

    def click(self, nth: int = 0, **kwargs):
        with allure.step(f'Clicking "{self._name}" {self._type_of}'):
            locator = self.get_locator(nth, **kwargs)
            locator.click()

    def scroll_into_element(self, nth: int = 0, **kwargs):
        with allure.step(f'Scrolling into "{self._name}" {self._type_of}'):
            locator = self.get_locator(nth, **kwargs)
            locator.scroll_into_view_if_needed()
