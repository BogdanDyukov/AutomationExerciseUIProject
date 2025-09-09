from pages.authentication.account_deleted_page import AccountDeletedPage
from steps.authentication.base_account_notification_page_steps import BaseAccountNotificationPageSteps


class AccountDeletedPageSteps(BaseAccountNotificationPageSteps):
    def __init__(self, account_deleted_page: AccountDeletedPage):
        super().__init__(account_deleted_page)

