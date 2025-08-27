from pathlib import Path

from playwright.sync_api import expect

from elements.base_element import BaseElement


class FileInput(BaseElement):
    @property
    def type_of(self) -> str:
        return "file input"

    def set_input_files(self, file_path: str, nth: int = 0, **kwargs):
        locator = self.get_locator(nth, **kwargs)
        locator.set_input_files(file_path)

    def check_have_value(self, file_path: str, nth: int = 0, **kwargs):
        locator = self.get_locator(nth, **kwargs)
        filename = Path(file_path).name
        expect(locator).to_have_value(filename)
