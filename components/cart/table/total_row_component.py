from playwright.sync_api import Page

from components.base_component import BaseComponent
from elements.static.text import Text


class TotalRowComponent(BaseComponent):
    def __init__(self, page: Page):
        super().__init__(page)

        self._total_amount_text = Text(page, '//h4/b[text()="Total Amount"]', 'Total Amount')
        self._total_price_text = Text(page, '(//p[@class="cart_total_price"])[last()]', 'Total Price')

    def check_total_amount_text(self):
        self._total_amount_text.check_visible()
        self._total_amount_text.check_have_text('Total Amount')

    def check_total_price_text(self, total_price: int | None = None):
        self._total_price_text.check_visible()

        if total_price:
            self._total_price_text.check_have_text('Rs. ' + str(total_price))

    def check_all(self, total_price: int | None = None):
        self.check_total_amount_text()
        self.check_total_price_text(total_price)
