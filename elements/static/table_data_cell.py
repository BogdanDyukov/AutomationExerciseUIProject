from elements.base_element import BaseElement


class TableDataCell(BaseElement):
    @property
    def type_of(self) -> str:
        return "table data cell"
