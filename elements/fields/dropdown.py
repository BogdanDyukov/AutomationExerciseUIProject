from elements.base_element import BaseElement
from elements.mixins.check_value_mixin import CheckValueMixin


class Dropdown(BaseElement, CheckValueMixin):
    @property
    def type_of(self) -> str:
        return "dropdown"

    def select_option(self, value: str, nth: int = 0, **kwargs):
        locator = self.get_locator(nth, **kwargs)
        locator.select_option(value=value)
