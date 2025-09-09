from playwright.sync_api import Page

from components.base_component import BaseComponent
from components.products.product_card_component import ProductCardComponent
from elements.static.text import Text
from elements.static.title import Title
from tools.playwright.extractors import extract_product_ids_by_data_product_id


class ListOfProductCardsComponent(BaseComponent):
    def __init__(self, page: Page):
        super().__init__(page)

        self._locator_with_data_id = '//div[@class="productinfo text-center"]/a'

        self.product_card_component: ProductCardComponent = ProductCardComponent(page)

        self._title = Title(page, '//h2[contains(@class, "title")]', 'Title')

    def check_title(self, title: str):
        self._title.check_visible()
        self._title.check_have_text(title)

    def get_product_ids(self) -> list[int]:
        return extract_product_ids_by_data_product_id(self._page, self._locator_with_data_id)
