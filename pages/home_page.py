from playwright.sync_api import Page

from components.common.modal_dialog_component import ModalDialogComponent
from components.navigation.navbar_component import NavbarComponent
from components.interactions.subscribe_to_updates_component import SubscribeToUpdatesComponent
from components.products.list_of_product_cards_component import ListOfProductCardsComponent
from data.modal_dialog import added_to_cart_modal
from elements.clickable.link import Link
from pages.base.base_page import BasePage
from config.routes import AppRoute


class HomePage(BasePage):
    def __init__(self, page: Page, path: AppRoute):
        super().__init__(page, path)

        self.navbar_component: NavbarComponent = NavbarComponent(page)
        self.list_of_product_cards_component: ListOfProductCardsComponent = ListOfProductCardsComponent(page)
        self.subscribe_to_updates_component: SubscribeToUpdatesComponent = SubscribeToUpdatesComponent(page)

        self.added_to_cart_modal_component: ModalDialogComponent = ModalDialogComponent(
            page=page,
            identifier='cartModal',
            data=added_to_cart_modal
        )

        self.scroll_up_link = Link(page, '//a[@id="scrollUp"]', 'Scroll Up')

    def check_scroll_up_link(self):
        self.scroll_up_link.check_visible()

    def click_scroll_up_link(self):
        self.scroll_up_link.click()

