from pages.home_page import HomePage
from pages.products.product_details_page import ProductDetailsPage
from pages.products.products_page import ProductsPage


class TestProducts:
    def test_all_product_list(
            self,
            home_page: HomePage,
            products_page: ProductsPage
    ):
        # 1 Открыть домашнюю страницу
        home_page.open()
        home_page.navbar_component.check_logo_link()

        # 2 Перейти на страницу со списком товаров
        home_page.navbar_component.click_products_link()
        products_page.is_open()
        products_page.list_of_product_cards_component.check_title('All Products')

        # 3 Проверить, что список товаров не пуст
        product_ids = products_page.list_of_product_cards_component.get_product_ids()
        assert len(product_ids) > 0, 'Product list is empty'

        # 4 Проверить, что отображается каждая карточка товара
        for product_id in product_ids:
            products_page.list_of_product_cards_component.product_card_component.check_all(product_id)

    def test_product_details(
            self,
            products_page: ProductsPage,
            product_details_page: ProductDetailsPage
    ):
        # 1 Перейти на страницу со списком товаров
        products_page.open()
        products_page.list_of_product_cards_component.check_title('All Products')

        # 2 Перейти на страницу с подробной информацией о первом товаре
        products_page.list_of_product_cards_component.product_card_component.click_view_product_button(product_id=1)
        product_details_page.is_open(product_id=1)

        # 3 Проверить, что отображаются соответствующие первому товару подробные сведения
        product_details_page.product_information_component.check_product_name_title('Blue Top')
        product_details_page.product_information_component.check_category_text('Women > Tops')
        product_details_page.product_information_component.check_price_text(500)
        product_details_page.product_information_component.check_availability_text('In Stock')
        product_details_page.product_information_component.check_condition_text('New')
        product_details_page.product_information_component.check_brand_text('Polo')
