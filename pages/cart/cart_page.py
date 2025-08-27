from playwright.sync_api import Page

from components.navigation.breadcrumb_component import BreadcrumbComponent
from components.navigation.navbar_component import NavbarComponent
from components.interactions.subscribe_to_updates_component import SubscribeToUpdatesComponent
from components.cart.table_cart_component import TableCartComponent
from elements.clickable.button import Button
from elements.clickable.link import Link
from elements.static.text import Text
from pages.base.base_page import BasePage
from config.routes import AppRoute


class CartPage(BasePage):
    def __init__(self, page: Page, path: AppRoute):
        super().__init__(page, path)

        self.navbar_component: NavbarComponent = NavbarComponent(page)
        self.breadcrumb_component: BreadcrumbComponent = BreadcrumbComponent(page, 'Home')
        self.table_cart_component: TableCartComponent = TableCartComponent(page)
        self.subscribe_to_updates_component: SubscribeToUpdatesComponent = SubscribeToUpdatesComponent(page)

        self.empty_cart_notification_text = Text(page, '//span[@id="empty_cart"]/p', 'Empty Cart Notification')

        self._here_link = Link(page, '//span[@id="empty_cart"]//a', 'Here')
        self._proceed_to_checkout_button = Button(page, '//a[text()="Proceed To Checkout"]', 'Proceed To Checkout')

    def check_empty_cart_notification_text(self):
        self.empty_cart_notification_text.check_visible()
        self.empty_cart_notification_text.check_have_text('Cart is empty! Click here to buy products.')

    def check_here_link(self):
        self._here_link.check_visible()
        self._here_link.check_have_text('here')

    def check_proceed_to_checkout_button(self):
        self._proceed_to_checkout_button.check_visible()
        self._proceed_to_checkout_button.check_have_text('Proceed To Checkout')

    def click_here_link(self):
        self._here_link.check_visible()
        self._here_link.click()

    def click_proceed_to_checkout_button(self):
        self._proceed_to_checkout_button.check_visible()
        self._proceed_to_checkout_button.click()
