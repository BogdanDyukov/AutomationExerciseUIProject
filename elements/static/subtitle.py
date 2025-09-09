from elements.base_element import BaseElement


# <h3>, <h4>
class Subtitle(BaseElement):
    @property
    def type_of(self) -> str:
        return 'subtitle'
