from elements.base_element import BaseElement
from elements.mixins.fillable_mixin import FillableMixin


class Textarea(BaseElement, FillableMixin):
    @property
    def type_of(self) -> str:
        return "textarea"
