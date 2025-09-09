from playwright.sync_api import Page

from components.base_component import BaseComponent
from elements.clickable.link import Link
from elements.static.text import Text


class EmptyCartViewComponent(BaseComponent):
    def __init__(self, page: Page):
        super().__init__(page)

        self.empty_cart_notification_text = Text(page, '//span[@id="empty_cart"]/p', 'Empty Cart Notification')

        self._here_link = Link(page, '//span[@id="empty_cart"]//a', 'Here')

    def check_empty_cart_notification_text(self):
        self.empty_cart_notification_text.check_visible()
        self.empty_cart_notification_text.check_have_text('Cart is empty! Click here to buy products.')

    def check_here_link(self):
        self._here_link.check_visible()
        self._here_link.check_have_text('here')

    def check_all(self):
        self.check_empty_cart_notification_text()
        self.check_here_link()

    def click_here_link(self):
        self._here_link.click()



