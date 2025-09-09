import re
from http import HTTPStatus

from playwright.sync_api import Page

from components.cart.table.product_row_component import ProductRowComponent
from elements.clickable.button import Button


class ProductRowWithButtonComponent(ProductRowComponent):
    def __init__(self, page: Page):
        super().__init__(page)

        self._product_delete_button = Button(page, '//a[@data-product-id="{product_id}"]', 'Product Delete')

    def check_product_delete_button(self, product_id: int):
        self._product_delete_button.check_visible(product_id=product_id)

    def check_all(
            self,
            product_id: int,
            name: str | None = None,
            category: str | None = None,
            price: str | None = None,
            total_price: str | None = None,
            quantity: int | None = None
    ):
        super().check_all(product_id, name, category, price, total_price, quantity)
        self.check_product_delete_button(product_id)

    # def click_product_delete_button(self, product_id: int):
    #     self._product_delete_button.click(product_id=product_id)

    def delete_product_from_cart(self, product_id: int):
        with self._page.expect_request(re.compile(r".*/delete_cart/.")) as first:
            self._product_delete_button.click(product_id=product_id)

        request = first.value
        assert request.response().status == HTTPStatus.OK
