from playwright.sync_api import Page

from components.base_component import BaseComponent
from elements.clickable.button import Button
from elements.media.image import Image
from elements.static.text import Text


class ProductCardComponent(BaseComponent):
    def __init__(self, page: Page):
        super().__init__(page)

        self._product_image = Image(page, '//img[@src="/get_product_picture/{product_id}"]', 'Product')
        self._price_title = Text(
            page, '(//a[@data-product-id="{product_id}"]/preceding-sibling::h2)[1]', 'Price Title'
        )
        self._product_name_text = Text(
            page, '(//a[@data-product-id="{product_id}"]/preceding-sibling::p)[1]', 'Product Name'
        )

        self._add_to_cart_button = Button(page, '(//a[@data-product-id="{product_id}"])[1]', 'Add To Cart')
        self._view_product_button = Button(page, '//a[@href="/product_details/{product_id}"]', 'View Product')

    def check_product_image(self, product_id: int):
        self._product_image.check_visible(product_id=product_id)

    def check_price_title(self, product_id: int, price_title: str | None = None):
        self._price_title.check_visible(product_id=product_id)

        if price_title:
            self._price_title.check_have_text(price_title, product_id=product_id)

    def check_product_name_text(self, product_id: int, product_name: str | None = None):
        self._product_name_text.check_visible(product_id=product_id)

        if product_name:
            self._product_name_text.check_have_text(product_name, product_id=product_id)

    def check_add_to_cart_button(self, product_id: int):
        self._add_to_cart_button.check_visible(product_id=product_id)
        self._add_to_cart_button.check_have_text('Add to cart', product_id=product_id)

    def check_view_product_button(self, product_id: int):
        self._view_product_button.check_visible(product_id=product_id)
        self._view_product_button.check_have_text('View Product', product_id=product_id)

    def check_all(
            self,
            product_id: int,
            price_title: str | None = None,
            product_name: str | None = None,
    ):
        self.check_product_image(product_id)
        self.check_price_title(product_id, price_title)
        self.check_product_name_text(product_id, product_name)
        self.check_add_to_cart_button(product_id)
        self.check_view_product_button(product_id)

    def click_add_to_cart_button(self, product_id: int):
        self._add_to_cart_button.check_visible(product_id=product_id)
        self._add_to_cart_button.click(product_id=product_id)

    def click_view_product_button(self, product_id: int):
        self._view_product_button.check_visible(product_id=product_id)
        self._view_product_button.click(product_id=product_id)
