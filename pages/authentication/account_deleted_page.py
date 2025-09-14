from playwright.sync_api import Page

from components.navigation.navbar_component import NavbarComponent
from components.authentication.account_notification_component import AccountNotificationComponent
from components.subscription.subscribe_to_updates_component import SubscribeToUpdatesComponent
from data.notifications import account_deleted_notification
from pages.base.base_page import BasePage
from config.routes import AppRoute


class AccountDeletedPage(BasePage):
    def __init__(self, page: Page, path: AppRoute):
        super().__init__(page, path)

        self.navbar_component: NavbarComponent = NavbarComponent(page)
        self.notification_component: AccountNotificationComponent = AccountNotificationComponent(
            page=page,
            identifier='account-deleted',
            data=account_deleted_notification
        )
        self.subscribe_to_updates_component: SubscribeToUpdatesComponent = SubscribeToUpdatesComponent(page)
