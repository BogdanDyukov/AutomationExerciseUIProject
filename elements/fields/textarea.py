from elements.base_element import BaseElement
from elements.mixins.check_value_mixin import CheckValueMixin
from elements.mixins.fillable_mixin import FillableMixin


class Textarea(BaseElement, FillableMixin, CheckValueMixin):
    @property
    def type_of(self) -> str:
        return "textarea"
