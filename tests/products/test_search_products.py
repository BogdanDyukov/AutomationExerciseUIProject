import pytest

from pages.home_page import HomePage
from pages.products.products_page import ProductsPage
from tools.api.api_client import check_products_for_query_match


class TestSearchProducts:
    @pytest.mark.parametrize('search_query', ['top'])
    def test_successful_search(self, home_page: HomePage, products_page: ProductsPage, search_query: str):
        # 1 Открыть домашнюю страницу
        home_page.open()
        home_page.navbar_component.check_logo_link()

        # 2 Перейти на страницу со списком товаров
        home_page.navbar_component.click_products_link()
        products_page.is_open()
        products_page.list_of_product_cards_component.check_title('All Products')

        # 3 Ввести поисковой запрос и нажать кнопку поиска
        products_page.search_field_component.fill_fields(search_query=search_query)
        products_page.search_field_component.click_submit_button()

        # 4 Проверить, что заголовок изменился соответствующим образом
        products_page.list_of_product_cards_component.check_title('Searched Products')

        product_ids = products_page.list_of_product_cards_component.get_product_ids()

        # 5 Проверить, что отображается каждая карточка товара
        for product_id in product_ids:
            products_page.list_of_product_cards_component.product_card_component.check_all(product_id)

        # 6 Проверить, что товары соответствуют поиску
        check_products_for_query_match(products_page.list_of_product_cards_component.get_product_ids(), search_query)
