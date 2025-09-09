from playwright.sync_api import Page

from components.base_component import BaseComponent
from elements.static.table_data_cell import TableDataCell


class TableHeaderComponent(BaseComponent):
    def __init__(self, page: Page):
        super().__init__(page)

        self._image_header_cell = TableDataCell(page, '(//tr[@class="cart_menu"]/td)[1]', 'Item Header')
        self._description_header_cell = TableDataCell(page, '(//tr[@class="cart_menu"]/td)[2]', 'Description Header')
        self._price_header_cell = TableDataCell(page, '(//tr[@class="cart_menu"]/td)[3]', 'Price Header')
        self._quantity_header_cell = TableDataCell(page, '(//tr[@class="cart_menu"]/td)[4]', 'Quantity Header')
        self._total_header_cell = TableDataCell(page, '(//tr[@class="cart_menu"]/td)[5]', 'Total Header')

    def check_image_header_cell(self):
        self._image_header_cell.check_visible()
        self._image_header_cell.check_have_text('Item')

    def check_description_header_cell(self):
        self._description_header_cell.check_visible()
        self._description_header_cell.check_have_text('Description')

    def check_price_header_cell(self):
        self._price_header_cell.check_visible()
        self._price_header_cell.check_have_text('Price')

    def check_quantity_header_cell(self):
        self._quantity_header_cell.check_visible()
        self._quantity_header_cell.check_have_text('Quantity')

    def check_total_header_cell(self):
        self._total_header_cell.check_visible()
        self._total_header_cell.check_have_text('Total')

    def check_all(self):
        self.check_image_header_cell()
        self.check_description_header_cell()
        self.check_price_header_cell()
        self.check_quantity_header_cell()
        self.check_total_header_cell()
