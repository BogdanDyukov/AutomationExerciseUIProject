from playwright.sync_api import Page

from components.cart.empty_cart_view_component import EmptyCartViewComponent
from components.common.modal_dialog_component import ModalDialogComponent
from components.navigation.breadcrumb_component import BreadcrumbComponent
from components.navigation.navbar_component import NavbarComponent
from components.interactions.subscribe_to_updates_component import SubscribeToUpdatesComponent
from components.cart.table.table_cart_component import TableCartComponent
from data.breadcrumb import cart_page_breadcrumb
from data.modal_dialog import checkout_modal
from elements.clickable.button import Button
from pages.base.base_page import BasePage
from config.routes import AppRoute


class CartPage(BasePage):
    def __init__(self, page: Page, path: AppRoute):
        super().__init__(page, path)

        self.navbar_component: NavbarComponent = NavbarComponent(page)
        self.breadcrumb_component: BreadcrumbComponent = BreadcrumbComponent(
            page=page,
            identifier='Home',
            data=cart_page_breadcrumb
        )
        self.empty_cart_notice_component: EmptyCartViewComponent = EmptyCartViewComponent(page)
        self.table_cart_component: TableCartComponent = TableCartComponent(page)
        self.subscribe_to_updates_component: SubscribeToUpdatesComponent = SubscribeToUpdatesComponent(page)

        self.checkout_modal_component: ModalDialogComponent = ModalDialogComponent(
            page=page,
            identifier='checkoutModal',
            data=checkout_modal
        )

        self._proceed_to_checkout_button = Button(page, '//a[text()="Proceed To Checkout"]', 'Proceed To Checkout')

    def check_proceed_to_checkout_button(self):
        self._proceed_to_checkout_button.check_visible()
        self._proceed_to_checkout_button.check_have_text('Proceed To Checkout')

    def click_proceed_to_checkout_button(self):
        self._proceed_to_checkout_button.click()
