from elements.base_element import BaseElement
from elements.mixins.disableable_mixin import DisableableMixin
from elements.mixins.fillable_mixin import FillableMixin


class Input(BaseElement, DisableableMixin, FillableMixin):
    @property
    def _type_of(self) -> str:
        return "input"
