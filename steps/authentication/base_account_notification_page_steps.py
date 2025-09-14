from pages.authentication.account_created_page import AccountCreatedPage
from pages.authentication.account_deleted_page import AccountDeletedPage


class BaseAccountNotificationPageSteps:
    def __init__(self, page: AccountCreatedPage | AccountDeletedPage):
        self._page = page

    def open_page(self):
        self._page.open()
        self._page.notification_component.check_title()

    def is_open_page(self):
        self._page.is_open()
        self._page.notification_component.check_title()

    def confirm_notification(self):
        self._page.notification_component.click_continue_button()
