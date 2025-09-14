from playwright.sync_api import Page

from components.common.modal_dialog_component import ModalDialogComponent
from components.products.list_of_product_cards_component import ListOfProductCardsComponent
from components.navigation.navbar_component import NavbarComponent
from components.products.search_field_component import SearchFieldComponent
from components.subscription.subscribe_to_updates_component import SubscribeToUpdatesComponent
from data.modal_dialog import added_to_cart_modal
from elements.media.image import Image
from pages.base.base_page import BasePage
from config.routes import AppRoute


class ProductsPage(BasePage):
    def __init__(self, page: Page, path: AppRoute):
        super().__init__(page, path)

        self.navbar_component: NavbarComponent = NavbarComponent(page)
        self.search_field_component: SearchFieldComponent = SearchFieldComponent(page)
        self.list_of_product_cards_component: ListOfProductCardsComponent = ListOfProductCardsComponent(page)
        self.subscribe_to_updates_component: SubscribeToUpdatesComponent = SubscribeToUpdatesComponent(page)

        self.added_to_cart_modal_component: ModalDialogComponent = ModalDialogComponent(
            page=page,
            identifier='cartModal',
            data=added_to_cart_modal
        )

        self._sale_image = Image(page, '//img[@id="sale_image"]', 'Sale')

    def check_sale_image(self):
        self._sale_image.check_visible()
