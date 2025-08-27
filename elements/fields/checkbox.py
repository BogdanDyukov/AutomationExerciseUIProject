from elements.base_element import BaseElement
from elements.mixins.checkable_mixin import CheckableMixin


class Checkbox(BaseElement, CheckableMixin):
    @property
    def type_of(self) -> str:
        return "checkbox"
