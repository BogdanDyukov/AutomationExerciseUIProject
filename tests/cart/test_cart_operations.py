import allure
import pytest

from steps.cart.cart_page_steps import CartPageSteps
from steps.home_page_steps import HomePageSteps
from steps.products.product_details_page_steps import ProductDetailsPageSteps
from steps.products.products_page_steps import ProductsPageSteps
from tools.allure.epics import AllureEpic
from tools.allure.features import AllureFeature
from tools.allure.stories import AllureStory


@pytest.mark.regression
@pytest.mark.cart
@allure.epic(AllureEpic.SHOPPING_CART)
@allure.feature(AllureFeature.CART_OPERATIONS)
@allure.parent_suite(AllureEpic.SHOPPING_CART)
@allure.suite(AllureFeature.CART_OPERATIONS)
class TestCartOperations:
    @pytest.mark.parametrize('added_product_ids', [[1, 2]])
    @allure.story(AllureStory.ADD_PRODUCT)
    @allure.sub_suite(AllureStory.ADD_PRODUCT)
    @allure.title('Checking adding products to the cart with an id: {added_product_ids}')
    @allure.severity(allure.severity_level.CRITICAL)
    def test_add_products_in_cart(
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
    @allure.story(AllureStory.ADD_PRODUCT)
    @allure.sub_suite(AllureStory.ADD_PRODUCT)
    @allure.title('Checking adding products to the cart with an id: {added_product_ids} and quantity: {quantity}')
    @allure.severity(allure.severity_level.NORMAL)
    def test_add_product_with_quantity(
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
    @allure.story(AllureStory.REMOVE_PRODUCT)
    @allure.sub_suite(AllureStory.REMOVE_PRODUCT)
    @allure.title('Checking remove product from cart')
    @allure.severity(allure.severity_level.CRITICAL)
    def test_remove_products_from_cart(
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
