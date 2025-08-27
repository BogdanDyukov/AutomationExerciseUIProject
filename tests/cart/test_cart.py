from pages.cart.cart_page import CartPage
from pages.home_page import HomePage
from pages.products.product_details_page import ProductDetailsPage
from pages.products.products_page import ProductsPage


class TestCart:
    def test_add_products_in_cart(self, home_page: HomePage, products_page: ProductsPage, cart_page: CartPage):
        # 1 Открыть домашнюю страницу
        home_page.open()
        home_page.navbar_component.check_logo_link()

        # 2 Перейти на страницу со списком товаров
        home_page.navbar_component.click_products_link()
        products_page.is_open()
        products_page.list_of_product_cards_component.check_title('All Products')

        # 3 Добавить первый товар в корзину и скрыть модальное окно
        products_page.list_of_product_cards_component.product_card_component.click_add_to_cart_button(product_id=1)
        products_page.added_to_cart_modal_component.click_continue_shopping_button()

        # 4 Добавить второй товар в корзину и с помощью модального окна перейти в корзину
        products_page.list_of_product_cards_component.product_card_component.click_add_to_cart_button(product_id=2)
        products_page.added_to_cart_modal_component.click_view_cart_link()
        cart_page.is_open()

        # 5 Проверить, что число товаров в корзине равняется двум
        assert len(cart_page.table_cart_component.get_product_ids()) == 2, 'Expected: Both items added to cart'

        # 6 Проверить цену, количество и общую стоимость для первого товара в корзине
        cart_page.table_cart_component.table_cart_row_component.check_product_price_text(product_id=1, price=500)
        cart_page.table_cart_component.table_cart_row_component.check_product_quantity_button(product_id=1, quantity=1)
        cart_page.table_cart_component.table_cart_row_component.check_product_total_price_text(
            product_id=1, total_price=500
        )

        # 7 Проверить цену, количество и общую стоимость для второго товара в корзине
        cart_page.table_cart_component.table_cart_row_component.check_product_price_text(product_id=2, price=400)
        cart_page.table_cart_component.table_cart_row_component.check_product_quantity_button(product_id=2, quantity=1)
        cart_page.table_cart_component.table_cart_row_component.check_product_total_price_text(
            product_id=2, total_price=400
        )

    def test_product_quantity_in_cart(
            self,
            products_page: ProductsPage,
            product_details_page: ProductDetailsPage,
            cart_page: CartPage
    ):
        # 1 Открыть страницу со списком товаров
        products_page.open()
        products_page.list_of_product_cards_component.check_title('All Products')

        # 2 Перейти на страницу подробных сведений о первом товаре
        products_page.list_of_product_cards_component.product_card_component.click_view_product_button(product_id=1)
        product_details_page.is_open(product_id=1)

        # 3 Проверить отображение информации о товаре
        product_details_page.product_information_component.check_product_name_title('Blue Top')
        product_details_page.product_information_component.check_category_text('Women > Tops')
        product_details_page.product_information_component.check_price_text(500)
        product_details_page.product_information_component.check_availability_text('In Stock')
        product_details_page.product_information_component.check_condition_text('New')
        product_details_page.product_information_component.check_brand_text('Polo')

        # 4 Установить количество товара и добавить его в корзину
        product_details_page.product_information_component.fill_fields(quantity=4)
        product_details_page.product_information_component.click_add_to_cart_button()

        # 5 Проверить отображение модального окна и с его помощью перейти в корзину
        product_details_page.added_to_cart_modal_component.check_all()
        product_details_page.added_to_cart_modal_component.click_view_cart_link()

        # 6 Проверить отображение товара в корзине с точным количеством
        cart_page.table_cart_component.table_cart_row_component.check_all(product_id=1, quantity=4)
