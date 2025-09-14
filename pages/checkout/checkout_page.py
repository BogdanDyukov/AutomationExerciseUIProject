import allure
from playwright.sync_api import Page

from components.cart.table.table_cart_with_total_row_component import TableCartWithTotalRowComponent
from components.checkout.address_delivery_component import AddressDeliveryComponent
from components.checkout.order_comment_component import OrderCommentComponent
from components.subscription.subscribe_to_updates_component import SubscribeToUpdatesComponent
from components.navigation.breadcrumb_component import BreadcrumbComponent
from components.navigation.navbar_component import NavbarComponent
from config.routes import AppRoute
from data.breadcrumb import checkout_page_breadcrumb
from elements.clickable.button import Button
from elements.static.title import Title
from pages.base.base_page import BasePage


class CheckoutPage(BasePage):
    def __init__(self, page: Page, path: AppRoute):
        super().__init__(page, path)

        self.navbar_component: NavbarComponent = NavbarComponent(page)
        self.breadcrumb_component: BreadcrumbComponent = BreadcrumbComponent(
            page=page,
            identifier='Home',
            data=checkout_page_breadcrumb
        )
        self.address_delivery_component: AddressDeliveryComponent = AddressDeliveryComponent(page)
        self.table_cart_with_total_row_component: TableCartWithTotalRowComponent = TableCartWithTotalRowComponent(page)
        self.order_comment_component: OrderCommentComponent = OrderCommentComponent(page)
        self.subscribe_to_updates_component: SubscribeToUpdatesComponent = SubscribeToUpdatesComponent(page)

        self._address_details_title = Title(page, '(//section[@id="cart_items"]//h2)[1]', 'Address Details')
        self._review_order_title = Title(page, '(//section[@id="cart_items"]//h2)[2]', 'Review Order')

        self._place_order_button = Button(page, '//a[@href="/payment"]', 'Place Order')

    def check_address_details_title(self):
        expected_text = 'Address Details'
        with allure.step(f'Check visible address details title with text "{expected_text}"'):
            self._address_details_title.check_visible()
            self._address_details_title.check_have_text(expected_text)

    def check_review_order_title(self):
        expected_text = 'Review Your Order'
        with allure.step(f'Check visible review order title with text "{expected_text}"'):
            self._review_order_title.check_visible()
            self._review_order_title.check_have_text(expected_text)

    def check_place_order_button(self):
        expected_text = 'Place Order'
        with allure.step(f'Check visible place order button with text "{expected_text}"'):
            self._place_order_button.check_visible()
            self._place_order_button.check_have_text(expected_text)

    def click_place_order_button(self):
        self._place_order_button.click()
