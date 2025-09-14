import allure
from playwright.sync_api import Page

from components.base_component import BaseComponent
from elements.clickable.link import Link
from elements.static.text import Text


class EmptyCartViewComponent(BaseComponent):
    def __init__(self, page: Page):
        super().__init__(page)

        self._notification_text = Text(page, '//span[@id="empty_cart"]/p', 'Empty Cart Notification')

        self._here_link = Link(page, '//span[@id="empty_cart"]//a', 'Here')

    def check_notification_text(self):
        expected_text = 'Cart is empty! Click here to buy products.'

        with allure.step(f'Check visible empty cart view notification text "{expected_text}"'):
            self._notification_text.check_visible()
            self._notification_text.check_have_text(expected_text)

    def check_here_link(self):
        expected_text = 'here'

        with allure.step(f'Check visible empty cart view here link with text "{expected_text}"'):
            self._here_link.check_visible()
            self._here_link.check_have_text(expected_text)

    def click_here_link(self):
        self._here_link.click()
