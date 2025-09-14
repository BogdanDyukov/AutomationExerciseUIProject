from pathlib import Path

import allure
from playwright.sync_api import expect

from elements.base_element import BaseElement


class FileInput(BaseElement):
    @property
    def _type_of(self) -> str:
        return "file input"

    def set_input_files(self, file_path: str, validate_value: bool = False, nth: int = 0, **kwargs):
        with allure.step(
                f'Set file "{file_path}" to the "{self._name}" {self._type_of} '
                f'{"with" if validate_value else "without"} validation'
        ):
            locator = self.get_locator(nth, **kwargs)
            locator.set_input_files(file_path)

            if validate_value:
                self.check_have_value(file_path, nth, **kwargs)

    def check_have_value(self, file_path: str, nth: int = 0, **kwargs):
        filename = Path(file_path).name

        with allure.step(f'Checking that "{self._name}" {self._type_of} has a value "{filename}"'):
            locator = self.get_locator(nth, **kwargs)
            expect(locator).to_have_value(filename)
