from elements.base_element import BaseElement


# <p>, <span>, <div>
# Всё, что является обычным текстовым блоком без семантики заголовка
class Text(BaseElement):
    @property
    def _type_of(self) -> str:
        return "text"
