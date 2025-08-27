from playwright.sync_api import Page

from components.base_component import BaseComponent
from components.products.product_card_component import ProductCardComponent
from elements.static.text import Text
from tools.playwright.extractors import extract_product_ids


class ListOfProductCardsComponent(BaseComponent):
    def __init__(self, page: Page):
        super().__init__(page)

        self._locator_with_data_id = '//div[@class="productinfo text-center"]/a'

        self.product_card_component: ProductCardComponent = ProductCardComponent(page)

        self._title = Text(page, '//h2[contains(@class, "title")]', 'Title')

    def check_title(self, title: str):
        self._title.check_visible()
        self._title.check_have_text(title)

    def get_product_ids(self) -> set[int]:
        return extract_product_ids(self._page, self._locator_with_data_id)
