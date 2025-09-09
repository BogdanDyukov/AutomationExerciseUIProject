from playwright.sync_api import Page

from components.base_component import BaseComponent
from components.cart.table.product_row_component import ProductRowComponent
from components.cart.table.table_header_component import TableHeaderComponent
from components.cart.table.total_row_component import TotalRowComponent
from tools.playwright.extractors import extract_product_ids_by_href


class TableCartWithTotalRowComponent(BaseComponent):
    def __init__(self, page: Page):
        super().__init__(page)

        self._locator_with_data_id = '//a[contains(@href, "/product_details")]'

        self.table_header_component: TableHeaderComponent = TableHeaderComponent(page)
        self.product_row_component: ProductRowComponent = ProductRowComponent(page)
        self.total_row_component: TotalRowComponent = TotalRowComponent(page)

    def get_product_ids(self) -> list[int]:
        return extract_product_ids_by_href(self._page, self._locator_with_data_id)
