import allure

from elements.base_element import BaseElement
from elements.mixins.fillable_mixin import FillableMixin


class Dropdown(BaseElement, FillableMixin):
    @property
    def _type_of(self) -> str:
        return "dropdown"

    def select_option(self, value: str, validate_value: bool = False, nth: int = 0, **kwargs):
        with allure.step(
                f'Selecting "{self._name}" {self._type_of} option '
                f'{"with" if validate_value else "without"} validation'
        ):
            locator = self.get_locator(nth, **kwargs)
            locator.select_option(value=value)

            if validate_value:
                self.check_have_value(value)
