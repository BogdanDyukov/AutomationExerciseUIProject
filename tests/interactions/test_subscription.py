from pages.cart.cart_page import CartPage
from pages.home_page import HomePage


class TestSubscription:
    def test_successful_subscription_on_home_page(self, home_page: HomePage):
        home_page.open()
        home_page.navbar_component.check_logo_link()
        home_page.subscribe_to_updates_component.check_title()
        home_page.subscribe_to_updates_component.fill_fields(email='user@mail.ru')
        home_page.subscribe_to_updates_component.click_subscribe_button()
        home_page.subscribe_to_updates_component.check_success_subscribe_alert()

    def test_successful_subscription_on_cart_page(self, cart_page: CartPage):
        cart_page.open()
        cart_page.breadcrumb_component.check_breadcrumb_current_item()
        cart_page.subscribe_to_updates_component.check_title()
        cart_page.subscribe_to_updates_component.fill_fields(email='user@mail.ru')
        cart_page.subscribe_to_updates_component.click_subscribe_button()
        cart_page.subscribe_to_updates_component.check_success_subscribe_alert()
