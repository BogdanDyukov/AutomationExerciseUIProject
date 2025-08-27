from playwright.sync_api import Page

from components.navigation.breadcrumb_component import BreadcrumbComponent
from components.cart.added_to_cart_modal_component import AddedToCartModalComponent
from components.products.list_of_product_cards_component import ListOfProductCardsComponent
from components.navigation.navbar_component import NavbarComponent
from components.products.search_field_component import SearchFieldComponent
from components.interactions.subscribe_to_updates_component import SubscribeToUpdatesComponent
from elements.media.image import Image
from pages.base.base_page import BasePage
from config.routes import AppRoute


class ProductsPage(BasePage):
    def __init__(self, page: Page, path: AppRoute):
        super().__init__(page, path)

        self.navbar_component: NavbarComponent = NavbarComponent(page)
        self.breadcrumb_component: BreadcrumbComponent = BreadcrumbComponent(page, 'Products')
        self.search_field_component: SearchFieldComponent = SearchFieldComponent(page)
        self.list_of_product_cards_component: ListOfProductCardsComponent = ListOfProductCardsComponent(page)
        self.subscribe_to_updates_component: SubscribeToUpdatesComponent = SubscribeToUpdatesComponent(page)

        self.added_to_cart_modal_component: AddedToCartModalComponent = AddedToCartModalComponent(page)

        self._sale_image = Image(page, '//img[@id="sale_image"]', 'Sale')

    def check_sale_image(self):
        self._sale_image.check_visible()
