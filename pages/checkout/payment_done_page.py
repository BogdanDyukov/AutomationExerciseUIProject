from playwright.sync_api import Page

from components.interactions.subscribe_to_updates_component import SubscribeToUpdatesComponent
from components.navigation.navbar_component import NavbarComponent
from components.checkout.order_confirmed_notification_component import OrderConfirmedNotificationComponent
from config.routes import AppRoute
from data.notifications import order_placed_notification
from pages.base.base_dynamic_page import BaseDynamicPage


class PaymentDonePage(BaseDynamicPage):
    def __init__(self, page: Page, path: AppRoute):
        super().__init__(page, path)

        self.navbar_component: NavbarComponent = NavbarComponent(page)
        self.order_notification_component: OrderConfirmedNotificationComponent = OrderConfirmedNotificationComponent(
            page=page,
            identifier='order-placed',
            data=order_placed_notification
        )
        self.subscribe_to_updates_component: SubscribeToUpdatesComponent = SubscribeToUpdatesComponent(page)
