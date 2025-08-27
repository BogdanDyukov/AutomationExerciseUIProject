from playwright.sync_api import Page

from components.base_component import BaseComponent
from elements.clickable.button import Button
from elements.media.image import Image
from elements.clickable.link import Link
from elements.static.text import Text


class TableCartRowComponent(BaseComponent):
    def __init__(self, page: Page):
        super().__init__(page)

        self._product_image = Image(page, '//img[@src="get_product_picture/{product_id}"]', 'Product')
        self._product_category_text = Text(
            page, '//a[@href="/product_details/{product_id}"]/parent::h4/parent::td/p', 'Product Category'
        )
        self._product_price_text = Text(
            page, '(//a[@data-product-id="{product_id}"]/parent::td/parent::tr/td)[3]//p', 'Product Price'
        )
        self._product_total_price_text = Text(
            page, '(//a[@data-product-id="{product_id}"]/parent::td/parent::tr/td)[5]//p', 'Product Total Price'
        )

        self._product_name_link = Link(page, '//a[@href="/product_details/{product_id}"]', 'Product Name')
        self._product_quantity_button = Button(
            page, '(//a[@data-product-id="{product_id}"]/parent::td/parent::tr/td)[4]//button', 'Product Quantity'
        )
        self._product_delete_button = Button(page, '//a[@data-product-id="{product_id}"]', 'Product Delete')

    # --- Checks ---
    def check_product_image(self, product_id: int):
        self._product_image.check_visible(product_id=product_id)

    def check_product_category_text(self, product_id: int, category: str | None = None):
        self._product_category_text.check_visible(product_id=product_id)

        if category:
            self._product_category_text.check_have_text(category, product_id=product_id)

    def check_product_price_text(self, product_id: int, price: int | None = None):
        self._product_price_text.check_visible(product_id=product_id)

        if price:
            self._product_price_text.check_have_text('Rs. ' + str(price), product_id=product_id)

    def check_product_total_price_text(self, product_id: int, total_price: int | None = None):
        self._product_total_price_text.check_visible(product_id=product_id)

        if total_price:
            self._product_total_price_text.check_have_text('Rs. ' + str(total_price), product_id=product_id)

    def check_product_name_link(self, product_id: int, name: str | None = None):
        self._product_name_link.check_visible(product_id=product_id)

        if name:
            self._product_name_link.check_have_text(name, product_id=product_id)

    def check_product_quantity_button(self, product_id: int, quantity: int | None = None):
        self._product_quantity_button.check_visible(product_id=product_id)

        if quantity:
            self._product_quantity_button.check_have_text(str(quantity), product_id=product_id)

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
        self.check_product_image(product_id)
        self.check_product_name_link(product_id, name)
        self.check_product_category_text(product_id, category)
        self.check_product_price_text(product_id, price)
        self.check_product_total_price_text(product_id, total_price)
        self.check_product_quantity_button(product_id, quantity)
        self.check_product_delete_button(product_id)

    # --- Actions ---
    def click_product_name_link(self, product_id: int):
        self._product_name_link.check_visible(product_id=product_id)
        self._product_name_link.click(product_id=product_id)

    def click_product_delete_button(self, product_id: int):
        self._product_delete_button.check_visible(product_id=product_id)
        self._product_delete_button.click(product_id=product_id)
