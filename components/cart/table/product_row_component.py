import allure
from playwright.sync_api import Page

from components.base_component import BaseComponent
from elements.clickable.button import Button
from elements.media.image import Image
from elements.clickable.link import Link
from elements.static.text import Text


class ProductRowComponent(BaseComponent):
    def __init__(self, page: Page):
        super().__init__(page)

        self._image = Image(page, '//img[@src="get_product_picture/{product_id}"]', 'Product')
        self._category_text = Text(
            page, '//a[@href="/product_details/{product_id}"]/parent::h4/parent::td/p', 'Product Category'
        )
        self._price_text = Text(
            page, '(//a[@data-product-id="{product_id}"]/parent::td/parent::tr/td)[3]//p', 'Product Price'
        )
        self._total_price_text = Text(
            page, '(//a[@data-product-id="{product_id}"]/parent::td/parent::tr/td)[5]//p', 'Product Total Price'
        )

        self._name_link = Link(page, '//a[@href="/product_details/{product_id}"]', 'Product Name')
        self._quantity_button = Button(
            page, '(//a[@data-product-id="{product_id}"]/parent::td/parent::tr/td)[4]//button', 'Product Quantity'
        )

    @allure.step('Check visible product row image with id "{product_id}"')
    def check_image(self, product_id: int):
        self._image.check_visible(product_id=product_id)

    @allure.step('Check visible product row category text with id "{product_id}"')
    def check_category_text(self, product_id: int, category: str | None = None):
        self._category_text.check_visible(product_id=product_id)

        if category:
            self._category_text.check_have_text(category, product_id=product_id)

    @allure.step('Check visible product row price text with id "{product_id}"')
    def check_price_text(self, product_id: int, price: int | None = None):
        self._price_text.check_visible(product_id=product_id)

        if price:
            self._price_text.check_have_text('Rs. ' + str(price), product_id=product_id)

    @allure.step('Check visible product row total price text with id "{product_id}"')
    def check_total_price_text(self, product_id: int, total_price: int | None = None):
        self._total_price_text.check_visible(product_id=product_id)

        if total_price:
            self._total_price_text.check_have_text('Rs. ' + str(total_price), product_id=product_id)

    @allure.step('Check visible product row name link with id "{product_id}"')
    def check_name_link(self, product_id: int, name: str | None = None):
        self._name_link.check_visible(product_id=product_id)

        if name:
            self._name_link.check_have_text(name, product_id=product_id)

    @allure.step('Check visible product row quantity button with id "{product_id}"')
    def check_quantity_button(self, product_id: int, quantity: int | None = None):
        self._quantity_button.check_visible(product_id=product_id)

        if quantity:
            self._quantity_button.check_have_text(str(quantity), product_id=product_id)

    @allure.step('Click product row name link with id "{product_id}"')
    def click_name_link(self, product_id: int):
        self._name_link.click(product_id=product_id)
