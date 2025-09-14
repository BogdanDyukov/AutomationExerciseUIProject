import allure
import pytest

from steps.home_page_steps import HomePageSteps
from steps.products.products_page_steps import ProductsPageSteps
from tools.allure.epics import AllureEpic
from tools.allure.features import AllureFeature
from tools.allure.stories import AllureStory


@pytest.mark.regression
@pytest.mark.products
@allure.epic(AllureEpic.PRODUCT_CATALOG)
@allure.feature(AllureFeature.PRODUCT_LISTING)
@allure.parent_suite(AllureEpic.PRODUCT_CATALOG)
@allure.suite(AllureFeature.PRODUCT_LISTING)
class TestProductList:
    @allure.story(AllureStory.VIEW_PRODUCT_LIST)
    @allure.sub_suite(AllureStory.VIEW_PRODUCT_LIST)
    @allure.title('Check the visibility of all product cards from the list')
    @allure.severity(allure.severity_level.CRITICAL)
    def test_all_product_list(
            self,
            home_page_steps: HomePageSteps,
            products_page_steps: ProductsPageSteps
    ):
        home_page_steps.open_page()
        home_page_steps.navbar.go_products()

        products_page_steps.is_open_page()
        products_page_steps.verify_all_product_cards()
