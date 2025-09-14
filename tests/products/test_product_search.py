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
@allure.feature(AllureFeature.PRODUCT_SEARCH)
@allure.parent_suite(AllureEpic.PRODUCT_CATALOG)
@allure.suite(AllureFeature.PRODUCT_SEARCH)
class TestProductSearch:
    @pytest.mark.parametrize('search_query', ['top'])
    @allure.story(AllureStory.SEARCH_PRODUCTS)
    @allure.title('Search products with a search query: "{search_query}"')
    @allure.severity(allure.severity_level.NORMAL)
    def test_successful_search(
            self,
            products_page_steps: ProductsPageSteps,
            home_page_steps: HomePageSteps,
            search_query: str
    ):
        home_page_steps.open_page()
        home_page_steps.navbar.go_products()

        products_page_steps.open_page()
        products_page_steps.find_products(search_query=search_query)
        products_page_steps.verify_product_cards_match_search(search_query=search_query)
