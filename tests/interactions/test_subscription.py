import allure
import pytest

from pages.cart.cart_page import CartPage
from pages.home_page import HomePage
from tools.allure.epics import AllureEpic
from tools.allure.features import AllureFeature
from tools.allure.stories import AllureStory


@pytest.mark.regression
@pytest.mark.subscription
@allure.epic(AllureEpic.INTERACTIONS)
@allure.feature(AllureFeature.SUBSCRIPTION)
@allure.parent_suite(AllureEpic.INTERACTIONS)
@allure.suite(AllureFeature.SUBSCRIPTION)
class TestSubscription:
    @allure.story(AllureStory.HOME_SUBSCRIPTION)
    @allure.sub_suite(AllureStory.HOME_SUBSCRIPTION)
    @allure.title('Checking event subscriptions on the home page')
    @allure.severity(allure.severity_level.MINOR)
    def test_subscription_on_home_page(self, home_page_with_state: HomePage):
        home_page_with_state.open()
        home_page_with_state.navbar_component.check_logo_link()
        home_page_with_state.subscribe_to_updates_component.check_title()
        home_page_with_state.subscribe_to_updates_component.fill_fields(email='user@mail.ru')
        home_page_with_state.subscribe_to_updates_component.click_subscribe_button()
        home_page_with_state.subscribe_to_updates_component.check_success_subscribe_alert()

    @allure.story(AllureStory.CART_SUBSCRIPTION)
    @allure.sub_suite(AllureStory.CART_SUBSCRIPTION)
    @allure.title('Checking event subscriptions on the cart page')
    @allure.severity(allure.severity_level.MINOR)
    def test_subscription_on_cart_page(self, cart_page_with_state: CartPage):
        cart_page_with_state.open()
        cart_page_with_state.breadcrumb_component.check_breadcrumb_current_item()
        cart_page_with_state.subscribe_to_updates_component.check_title()
        cart_page_with_state.subscribe_to_updates_component.fill_fields(email='user@mail.ru')
        cart_page_with_state.subscribe_to_updates_component.click_subscribe_button()
        cart_page_with_state.subscribe_to_updates_component.check_success_subscribe_alert()
