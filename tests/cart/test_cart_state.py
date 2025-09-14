import allure
import pytest

from models.test_user import TestUser
from steps.cart.cart_page_steps import CartPageSteps
from steps.home_page_steps import HomePageSteps
from steps.authentication.signup_or_login_page_steps import SignupOrLoginPageSteps
from steps.products.products_page_steps import ProductsPageSteps
from tools.allure.epics import AllureEpic
from tools.allure.features import AllureFeature
from tools.allure.stories import AllureStory


@pytest.mark.regression
@pytest.mark.cart
@allure.epic(AllureEpic.SHOPPING_CART)
@allure.feature(AllureFeature.CART_STATE)
@allure.parent_suite(AllureEpic.SHOPPING_CART)
@allure.suite(AllureFeature.CART_STATE)
class TestCartState:
    @pytest.mark.parametrize('search_query', ['Blue Top'])
    @allure.story(AllureStory.CART_CONSISTENT)
    @allure.sub_suite(AllureStory.CART_CONSISTENT)
    @allure.title('Checking the identity of the cart before and after logging')
    @allure.severity(allure.severity_level.NORMAL)
    def test_cart_consistent_before_and_after_login(
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
