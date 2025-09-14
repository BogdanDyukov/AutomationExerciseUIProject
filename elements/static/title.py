from elements.base_element import BaseElement


# <h1>, <h2>
class Title(BaseElement):
    @property
    def _type_of(self) -> str:
        return 'title'
