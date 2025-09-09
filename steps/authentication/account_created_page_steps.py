from pages.authentication.account_created_page import AccountCreatedPage
from steps.authentication.base_account_notification_page_steps import BaseAccountNotificationPageSteps


class AccountCreatedPageSteps(BaseAccountNotificationPageSteps):
    def __init__(self, account_created_page: AccountCreatedPage):
        super().__init__(account_created_page)

