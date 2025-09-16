from pages.products.products_page import ProductsPage
from tools.api.products import check_products_for_query_match


class ProductsPageSteps:
    def __init__(self, products_page: ProductsPage):
        self._products_page = products_page

    def open_page(self):
        self._products_page.open()
        self._products_page.check_sale_image()
        self._products_page.list_of_product_cards_component.check_title('All Products')

    def is_open_page(self):
        self._products_page.is_open()
        self._products_page.check_sale_image()
        self._products_page.list_of_product_cards_component.check_title('All Products')

    def add_products_to_cart(self, product_ids: list[int], redirect_to_cart_page: bool = False):

        for index in range(len(product_ids) - 1):
            self._products_page.list_of_product_cards_component.product_card_component.click_add_to_cart_button(
                product_id=product_ids[index]
            )
            self._products_page.added_to_cart_modal_component.click_continue_button()

        self._products_page.list_of_product_cards_component.product_card_component.click_add_to_cart_button(
            product_id=product_ids[len(product_ids) - 1]
        )

        if redirect_to_cart_page:
            self._products_page.added_to_cart_modal_component.click_navigation_link()
        else:
            self._products_page.added_to_cart_modal_component.click_continue_button()

    def add_all_products_to_cart(self, redirect_to_cart_page: bool = False) -> list[int]:
        product_ids = self._products_page.list_of_product_cards_component.get_product_ids()
        self.add_products_to_cart(product_ids=list(product_ids), redirect_to_cart_page=redirect_to_cart_page)
        return product_ids

    def view_product_details(self, product_id: int):
        self._products_page.list_of_product_cards_component.product_card_component.click_view_product_button(product_id)

    def verify_product_cards_match_search(self, search_query: str = ''):
        product_ids = self._products_page.list_of_product_cards_component.get_product_ids()
        check_products_for_query_match(product_ids, search_query)

    def verify_all_product_cards(self):
        self.verify_product_cards_match_search(search_query='')

    def find_products(self, search_query: str):
        self._products_page.search_field_component.fill_fields(search_query=search_query)
        self._products_page.search_field_component.click_submit_button()

        self._products_page.list_of_product_cards_component.check_title('Searched Products')
