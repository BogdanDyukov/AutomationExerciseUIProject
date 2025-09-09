from pages.home_page import HomePage
from steps.navbar_component_steps import NavbarComponentSteps


class HomePageSteps:
    def __init__(self, home_page: HomePage):
        self.navbar = NavbarComponentSteps(home_page.navbar_component)

        self._home_page = home_page

    def open_page(self):
        self._home_page.open()
        self._home_page.list_of_product_cards_component.check_title('Features Items')

    def is_open_page(self):
        self._home_page.is_open()
        self._home_page.list_of_product_cards_component.check_title('Features Items')

    def add_products_to_cart(self, product_ids: list[int], redirect_to_cart_page: bool = False):

        for index in range(len(product_ids) - 1):
            self._home_page.list_of_product_cards_component.product_card_component.click_add_to_cart_button(
                product_id=product_ids[index]
            )
            self._home_page.added_to_cart_modal_component.click_continue_button()

        self._home_page.list_of_product_cards_component.product_card_component.click_add_to_cart_button(
            product_id=product_ids[len(product_ids) - 1]
        )

        if redirect_to_cart_page:
            self._home_page.added_to_cart_modal_component.click_navigation_link()
        else:
            self._home_page.added_to_cart_modal_component.click_continue_button()
