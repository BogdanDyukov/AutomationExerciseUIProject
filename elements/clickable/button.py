from elements.base_element import BaseElement
from elements.mixins.disableable_mixin import DisableableMixin


class Button(BaseElement, DisableableMixin):
    @property
    def type_of(self) -> str:
        return "button"
