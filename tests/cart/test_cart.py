import pytest

from models.test_user import TestUser
from pages.authentication.signup_or_login_page import SignupOrLoginPage
from pages.cart.cart_page import CartPage
from pages.home_page import HomePage
from pages.products.product_details_page import ProductDetailsPage
from pages.products.products_page import ProductsPage
from steps.cart.cart_page_steps import CartPageSteps
from steps.home_page_steps import HomePageSteps
from steps.authentication.signup_or_login_page_steps import SignupOrLoginPageSteps
from steps.products.product_details_page_steps import ProductDetailsPageSteps
from steps.products.products_page_steps import ProductsPageSteps
from tools.api.api_client import check_products_for_query_match


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
        products_page.added_to_cart_modal_component.click_continue_button()

        # 4 Добавить второй товар в корзину и с помощью модального окна перейти в корзину
        products_page.list_of_product_cards_component.product_card_component.click_add_to_cart_button(product_id=2)
        products_page.added_to_cart_modal_component.click_navigation_link()
        cart_page.is_open()

        # 5 Проверить, что число товаров в корзине равняется двум
        assert len(cart_page.table_cart_component.get_product_ids()) == 2, 'Expected: Both items added to cart'

        # 6 Проверить цену, количество и общую стоимость для первого товара в корзине
        cart_page.table_cart_component.product_row_with_button_component.check_product_price_text(
            product_id=1,
            price=500
        )
        cart_page.table_cart_component.product_row_with_button_component.check_product_quantity_button(
            product_id=1,
            quantity=1
        )
        cart_page.table_cart_component.product_row_with_button_component.check_product_total_price_text(
            product_id=1, total_price=500
        )

        # 7 Проверить цену, количество и общую стоимость для второго товара в корзине
        cart_page.table_cart_component.product_row_with_button_component.check_product_price_text(
            product_id=2,
            price=400
        )
        cart_page.table_cart_component.product_row_with_button_component.check_product_quantity_button(
            product_id=2,
            quantity=1
        )
        cart_page.table_cart_component.product_row_with_button_component.check_product_total_price_text(
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
        product_details_page.product_information_component.check_all(
            product_name='Blue Top',
            category='Women > Tops',
            price=500,
            availability='In Stock',
            condition='New',
            brand='Polo',
            quantity=1
        )

        # 4 Установить количество товара и добавить его в корзину
        product_details_page.product_information_component.fill_fields(quantity=4)
        product_details_page.product_information_component.click_add_to_cart_button()

        # 5 Проверить отображение модального окна и с его помощью перейти в корзину
        product_details_page.added_to_cart_modal_component.check_all()
        product_details_page.added_to_cart_modal_component.click_navigation_link()

        # 6 Проверить отображение товара в корзине с точным количеством
        cart_page.table_cart_component.product_row_with_button_component.check_all(product_id=1, quantity=4)

    def test_remove_products_from_cart(self, home_page: HomePage, cart_page: CartPage):
        home_page.open()
        home_page.navbar_component.check_logo_link()
        home_page.list_of_product_cards_component.product_card_component.click_add_to_cart_button(product_id=1)
        home_page.added_to_cart_modal_component.click_continue_button()
        home_page.list_of_product_cards_component.product_card_component.click_add_to_cart_button(product_id=1)
        home_page.added_to_cart_modal_component.click_navigation_link()

        cart_page.is_open()
        cart_page.table_cart_component.table_header_component.check_all()
        cart_page.table_cart_component.product_row_with_button_component.click_product_delete_button(product_id=1)
        cart_page.empty_cart_notice_component.check_all()
        cart_page.reload()
        cart_page.empty_cart_notice_component.check_all()

    @pytest.mark.parametrize('search_query', ['Blue Top'])
    def test_cart_consistent_before_and_after_login(
            self,
            products_page: ProductsPage,
            cart_page: CartPage,
            signup_or_login_page: SignupOrLoginPage,
            home_page: HomePage,
            authorized_test_user: TestUser,
            search_query: str
    ):
        # 1 Перейти на страницу со списком товаров
        products_page.open()
        products_page.list_of_product_cards_component.check_title('All Products')

        # 2 Ввести поисковой запрос и нажать кнопку поиска
        products_page.search_field_component.fill_fields(search_query=search_query)
        products_page.search_field_component.click_submit_button()

        # 3 Проверить, что заголовок изменился соответствующим образом
        products_page.list_of_product_cards_component.check_title('Searched Products')

        product_ids = products_page.list_of_product_cards_component.get_product_ids()

        # 4 Проверить, что результаты соответствуют поиску
        check_products_for_query_match(product_ids, search_query)

        # 5 Добавить все найденные товары в корзину
        for product_id in product_ids:
            products_page.list_of_product_cards_component.product_card_component.click_add_to_cart_button(product_id)
            products_page.added_to_cart_modal_component.click_continue_button()

        # 6 Открыть страницу корзины
        products_page.navbar_component.click_cart_link()
        cart_page.is_open()

        # 7 Проверить, что добавленные товары отображаются в корзине
        for product_id in product_ids:
            cart_page.table_cart_component.product_row_with_button_component.check_all(product_id=product_id)

        # 8 Перейти на страницу авторизации и войти в аккаунт
        cart_page.navbar_component.click_signup_or_login_link()
        signup_or_login_page.is_open()
        signup_or_login_page.login_form_component.fill_fields(
            email=authorized_test_user.account_information.email,
            password=authorized_test_user.account_information.password
        )
        signup_or_login_page.login_form_component.click_login_button()

        # 9 Снова перейти на страницу корзины
        home_page.is_open()
        home_page.navbar_component.check_logged_in_user_text(authorized_test_user.account_information.name)
        home_page.navbar_component.click_cart_link()
        cart_page.is_open()

        # 10 Проверить, что те же товары также отображаются в корзине
        for product_id in product_ids:
            cart_page.table_cart_component.product_row_with_button_component.check_all(product_id=product_id)

    @pytest.mark.parametrize('added_product_ids', [[1, 2]])
    def test_add_products_in_cart_2(
            self,
            home_page_steps: HomePageSteps,
            products_page_steps: ProductsPageSteps,
            cart_page_steps: CartPageSteps,
            added_product_ids: list[int]
    ):
        home_page_steps.open_page()
        home_page_steps.navbar.go_products()

        products_page_steps.is_open_page()
        products_page_steps.add_products_to_cart(product_ids=added_product_ids, redirect_to_cart_page=True)

        cart_page_steps.is_open_page()
        cart_page_steps.verify_non_empty_cart(product_ids_in_cart=added_product_ids)

    @pytest.mark.parametrize('product_id, quantity', [(1, 3)])
    def test_product_quantity_in_cart_2(
            self,
            products_page_steps: ProductsPageSteps,
            product_details_page_steps: ProductDetailsPageSteps,
            cart_page_steps: CartPageSteps,
            product_id: int,
            quantity: int
    ):
        products_page_steps.open_page()
        products_page_steps.view_product_details(product_id=product_id)

        product_details_page_steps.is_open_page(product_id=product_id)
        product_details_page_steps.verify_product_details_displayed(
            product_id=product_id
        )
        product_details_page_steps.add_product_to_cart(
            quantity=quantity,
            redirect_to_cart_page=True
        )

        cart_page_steps.is_open_page()
        cart_page_steps.verify_non_empty_cart(product_ids_in_cart=[product_id]*quantity)

    @pytest.mark.parametrize('added_product_ids', [[1, 1, 2]])
    def test_remove_products_from_cart_2(
            self,
            home_page_steps: HomePageSteps,
            cart_page_steps: CartPageSteps,
            added_product_ids: list[int]
    ):
        home_page_steps.open_page()
        home_page_steps.add_products_to_cart(product_ids=added_product_ids, redirect_to_cart_page=True)

        cart_page_steps.is_open_page()
        cart_page_steps.verify_non_empty_cart(product_ids_in_cart=added_product_ids)
        cart_page_steps.delete_product_from_cart(product_id_to_delete=added_product_ids[0])

    @pytest.mark.parametrize('search_query', ['Blue Top'])
    def test_cart_consistent_before_and_after_login_2(
            self,
            home_page_steps: HomePageSteps,
            products_page_steps: ProductsPageSteps,
            cart_page_steps: CartPageSteps,
            signup_or_login_page_steps: SignupOrLoginPageSteps,
            authorized_test_user: TestUser,
            search_query: str
    ):
        products_page_steps.open_page()
        products_page_steps.find_products(search_query=search_query)
        products_page_steps.verify_product_cards_match_search(search_query=search_query)
        added_products = products_page_steps.add_all_products_to_cart(redirect_to_cart_page=True)

        cart_page_steps.is_open_page()
        cart_page_steps.verify_non_empty_cart(product_ids_in_cart=added_products)
        cart_page_steps.navbar.go_signup_or_login()

        signup_or_login_page_steps.is_open_page()
        signup_or_login_page_steps.login_to_account(
            email=authorized_test_user.account_information.email,
            password=authorized_test_user.account_information.password
        )

        home_page_steps.is_open_page()
        home_page_steps.navbar.go_cart()

        cart_page_steps.is_open_page()
        cart_page_steps.verify_non_empty_cart(product_ids_in_cart=added_products)
