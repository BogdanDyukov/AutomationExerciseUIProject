from elements.base_element import BaseElement
from elements.mixins.check_value_mixin import CheckValueMixin
from elements.mixins.disableable_mixin import DisableableMixin
from elements.mixins.fillable_mixin import FillableMixin


class Input(BaseElement, DisableableMixin, FillableMixin, CheckValueMixin):
    @property
    def type_of(self) -> str:
        return "input"
