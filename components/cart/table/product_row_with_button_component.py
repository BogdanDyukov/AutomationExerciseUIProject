import re
from http import HTTPStatus

import allure
from playwright.sync_api import Page

from components.cart.table.product_row_component import ProductRowComponent
from elements.clickable.button import Button


class ProductRowWithButtonComponent(ProductRowComponent):
    def __init__(self, page: Page):
        super().__init__(page)

        self._delete_button = Button(page, '//a[@data-product-id="{product_id}"]', 'Product Delete')

    @allure.step('Check visible product row delete button with id "{product_id}"')
    def check_delete_button(self, product_id: int):
        self._delete_button.check_visible(product_id=product_id)

    @allure.step('Delete product row with id "{product_id}"')
    def delete_product_from_cart(self, product_id: int):
        with self._page.expect_request(re.compile(r".*/delete_cart/.")) as first:
            self._delete_button.click(product_id=product_id)

        request = first.value
        assert request.response().status == HTTPStatus.OK
