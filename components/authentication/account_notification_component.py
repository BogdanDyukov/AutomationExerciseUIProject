import allure
from playwright.sync_api import Page

from components.base_notification_component import BaseNotificationComponent
from models.notification import Notification
from elements.static.text import Text


class AccountNotificationComponent(BaseNotificationComponent):
    def __init__(self, page: Page, identifier: str, data: Notification):
        super().__init__(page, identifier, data)

        self._additional_text = Text(page, '(//div[@class="col-sm-9 col-sm-offset-1"]/p)[2]', 'Additional')

    def check_additional_text(self):
        expected_text = self._data.additional_text

        with allure.step(f'Check visible notification additional text "{expected_text}"'):
            self._additional_text.check_visible()
            self._additional_text.check_have_text(expected_text)
