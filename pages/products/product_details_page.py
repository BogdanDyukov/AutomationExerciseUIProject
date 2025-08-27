from playwright.sync_api import Page

from components.cart.added_to_cart_modal_component import AddedToCartModalComponent
from components.products.product_information_component import ProductInformationComponent
from config.routes import AppRoute
from elements.media.image import Image
from pages.base.base_dynamic_page import BaseDynamicPage


class ProductDetailsPage(BaseDynamicPage):
    def __init__(self, page: Page, path: AppRoute):
        super().__init__(page, path)

        self.product_information_component = ProductInformationComponent(page)

        self.added_to_cart_modal_component: AddedToCartModalComponent = AddedToCartModalComponent(page)

        self._product_image = Image(page, '//div[@class="view-product"]//img', 'Product')

    def check_product_image(self):
        self._product_image.check_visible()
