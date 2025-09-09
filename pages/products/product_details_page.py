from playwright.sync_api import Page

from components.common.modal_dialog_component import ModalDialogComponent
from components.products.product_information_component import ProductInformationComponent
from components.products.product_review_form_component import ProductReviewFormComponent
from config.routes import AppRoute
from data.modal_dialog import added_to_cart_modal
from elements.media.image import Image
from pages.base.base_dynamic_page import BaseDynamicPage


class ProductDetailsPage(BaseDynamicPage):
    def __init__(self, page: Page, path: AppRoute):
        super().__init__(page, path)

        self.product_information_component: ProductInformationComponent = ProductInformationComponent(page)
        self.product_review_form_component: ProductReviewFormComponent = ProductReviewFormComponent(page)

        self.added_to_cart_modal_component: ModalDialogComponent = ModalDialogComponent(
            page=page,
            identifier='cartModal',
            data=added_to_cart_modal
        )

        self._product_image = Image(page, '//div[@class="view-product"]//img', 'Product')

    def check_product_image(self):
        self._product_image.check_visible()
