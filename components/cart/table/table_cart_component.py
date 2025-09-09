from playwright.sync_api import Page

from components.base_component import BaseComponent
from components.cart.table.product_row_with_button_component import ProductRowWithButtonComponent
from components.cart.table.table_header_component import TableHeaderComponent
from tools.playwright.extractors import extract_product_ids_by_data_product_id


class TableCartComponent(BaseComponent):
    def __init__(self, page: Page):
        super().__init__(page)

        self._locator_with_data_id = '//a[@data-product-id]'

        self.table_header_component: TableHeaderComponent = TableHeaderComponent(page)
        self.product_row_with_button_component: ProductRowWithButtonComponent = ProductRowWithButtonComponent(page)

    def get_product_ids(self) -> list[int]:
        return extract_product_ids_by_data_product_id(self._page, self._locator_with_data_id)
