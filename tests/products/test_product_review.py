import allure
import pytest

from steps.products.product_details_page_steps import ProductDetailsPageSteps
from steps.products.products_page_steps import ProductsPageSteps
from tools.allure.epics import AllureEpic
from tools.allure.features import AllureFeature
from tools.allure.stories import AllureStory


@pytest.mark.regression
@pytest.mark.products
@allure.epic(AllureEpic.PRODUCT_CATALOG)
@allure.feature(AllureFeature.PRODUCT_REVIEW)
@allure.parent_suite(AllureEpic.PRODUCT_CATALOG)
@allure.suite(AllureFeature.PRODUCT_REVIEW)
class TestProductReview:
    @pytest.mark.parametrize('product_id', [1])
    @allure.story(AllureStory.ADD_PRODUCT_REVIEW)
    @allure.sub_suite(AllureStory.ADD_PRODUCT_REVIEW)
    @allure.title('Adding a review to a product with an id {product_id}')
    @allure.severity(allure.severity_level.MINOR)
    def test_add_review_on_product(
            self,
            products_page_steps: ProductsPageSteps,
            product_details_page_steps: ProductDetailsPageSteps,
            product_id: int
    ):
        products_page_steps.open_page()
        products_page_steps.view_product_details(product_id=product_id)

        product_details_page_steps.is_open_page(product_id=product_id)
        product_details_page_steps.write_and_submit_review(
            name='Bogdan',
            email='user@mail.ru',
            review='Good quality top'
        )
