import allure
from playwright.sync_api import Page

from components.base_component import BaseComponent
from elements.static.table_data_cell import TableDataCell


class TableHeaderComponent(BaseComponent):
    def __init__(self, page: Page):
        super().__init__(page)

        self._image_cell = TableDataCell(page, '(//tr[@class="cart_menu"]/td)[1]', 'Item Header')
        self._description_cell = TableDataCell(page, '(//tr[@class="cart_menu"]/td)[2]', 'Description Header')
        self._price_cell = TableDataCell(page, '(//tr[@class="cart_menu"]/td)[3]', 'Price Header')
        self._quantity_cell = TableDataCell(page, '(//tr[@class="cart_menu"]/td)[4]', 'Quantity Header')
        self._total_cell = TableDataCell(page, '(//tr[@class="cart_menu"]/td)[5]', 'Total Header')

    def check_image_cell(self):
        expected_text = 'Item'

        with allure.step(f'Check visible table cell "Image" with text "{expected_text}"'):
            self._image_cell.check_visible()
            self._image_cell.check_have_text(expected_text)

    def check_description_cell(self):
        expected_text = 'Description'

        with allure.step(f'Check visible table cell "Description" with text "{expected_text}"'):
            self._description_cell.check_visible()
            self._description_cell.check_have_text(expected_text)

    def check_price_cell(self):
        expected_text = 'Price'

        with allure.step(f'Check visible table cell "Price" with text "{expected_text}"'):
            self._price_cell.check_visible()
            self._price_cell.check_have_text(expected_text)

    def check_quantity_cell(self):
        expected_text = 'Quantity'

        with allure.step(f'Check visible table cell "Quantity" with text "{expected_text}"'):
            self._quantity_cell.check_visible()
            self._quantity_cell.check_have_text(expected_text)

    def check_total_cell(self):
        expected_text = 'Total'

        with allure.step(f'Check visible table cell "Total" with text "{expected_text}"'):
            self._total_cell.check_visible()
            self._total_cell.check_have_text(expected_text)
