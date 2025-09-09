from playwright.sync_api import Page

from components.interactions.subscribe_to_updates_component import SubscribeToUpdatesComponent
from components.navigation.breadcrumb_component import BreadcrumbComponent
from components.navigation.navbar_component import NavbarComponent
from components.checkout.payment_form_component import PaymentFormComponent
from config.routes import AppRoute
from data.breadcrumb import payment_page_breadcrumb
from elements.static.title import Title
from pages.base.base_page import BasePage


class PaymentPage(BasePage):
    def __init__(self, page: Page, path: AppRoute):
        super().__init__(page, path)

        self.navbar_component: NavbarComponent = NavbarComponent(page)
        self.breadcrumb_component: BreadcrumbComponent = BreadcrumbComponent(
            page=page,
            identifier='Home',
            data=payment_page_breadcrumb
        )
        self.payment_form_component: PaymentFormComponent = PaymentFormComponent(page)
        self.subscribe_to_updates_component: SubscribeToUpdatesComponent = SubscribeToUpdatesComponent(page)

        self._title = Title(page, '//h2[text()="Payment"]', 'Title')

    def check_title(self):
        self._title.check_visible()
        self._title.check_have_text('Payment')
