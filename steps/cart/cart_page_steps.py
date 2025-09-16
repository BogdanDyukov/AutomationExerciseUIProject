from pages.cart.cart_page import CartPage
from steps.navbar_component_steps import NavbarComponentSteps
from tools.api.products import get_products_info


class CartPageSteps:
    def __init__(self, cart_page: CartPage):
        self.navbar = NavbarComponentSteps(cart_page.navbar_component)

        self._cart_page = cart_page

    def open_page(self):
        self._cart_page.open()
        self._cart_page.breadcrumb_component.check_breadcrumb_current_item()
        self._cart_page.breadcrumb_component.check_breadcrumb_home_item_link()

    def is_open_page(self):
        self._cart_page.is_open()
        self._cart_page.breadcrumb_component.check_breadcrumb_current_item()
        self._cart_page.breadcrumb_component.check_breadcrumb_home_item_link()

    def verify_empty_cart(self):
        self._cart_page.empty_cart_notice_component.check_notification_text()
        self._cart_page.empty_cart_notice_component.check_here_link()

    def verify_non_empty_cart(self, product_ids_in_cart: list[int]):
        assert len(self._cart_page.table_cart_component.get_product_ids()) == len(set(product_ids_in_cart)), \
            'The number of items in the basket does not match the transmitted'

        products_info = get_products_info(product_ids_in_cart)

        for product_info in products_info:
            product_id = int(product_info['id'])
            product_price = int(product_info['price'].split()[1])
            product_quantity = product_ids_in_cart.count(product_id)

            self._cart_page.table_cart_component.product_row_with_button_component.check_name_link(
                product_id=product_id,
                name=product_info['name']
            )
            self._cart_page.table_cart_component.product_row_with_button_component.check_category_text(
                product_id=product_id,
                category=product_info['category']['usertype']['usertype'] + ' > ' + product_info['category']['category']
            )
            self._cart_page.table_cart_component.product_row_with_button_component.check_price_text(
                product_id=product_id,
                price=product_price
            )
            self._cart_page.table_cart_component.product_row_with_button_component.check_quantity_button(
                product_id=product_id,
                quantity=product_quantity
            )
            self._cart_page.table_cart_component.product_row_with_button_component.check_total_price_text(
                product_id=product_id,
                total_price=product_quantity * product_price
            )

    def delete_product_from_cart(self, product_id_to_delete):
        product_ids_in_cart_before_delete = self._cart_page.table_cart_component.get_product_ids()

        assert product_id_to_delete in product_ids_in_cart_before_delete, \
            'The product with the transmitted id is not in the shopping cart'

        self._cart_page.table_cart_component.product_row_with_button_component.delete_product_from_cart(
            product_id=product_id_to_delete
        )

        product_ids_in_cart_after_delete = self._cart_page.table_cart_component.get_product_ids()

        assert (product_id_to_delete not in product_ids_in_cart_after_delete
                and len(product_ids_in_cart_before_delete) - 1 == len(product_ids_in_cart_after_delete)), \
            'The product with the transmitted id remained in the cart after delete.'

        if product_ids_in_cart_after_delete == 1:
            self._cart_page.empty_cart_notice_component.check_notification_text()
            self._cart_page.empty_cart_notice_component.check_here_link()
            self._cart_page.reload()
            self._cart_page.empty_cart_notice_component.check_notification_text()
            self._cart_page.empty_cart_notice_component.check_here_link()

    def proceed_to_checkout(self):
        self._cart_page.click_proceed_to_checkout_button()

    def try_proceed_to_checkout_without_logging(self, redirect_to_signup_or_login_page: bool = False):
        self.proceed_to_checkout()

        if redirect_to_signup_or_login_page:
            self._cart_page.checkout_modal_component.click_navigation_link()
        else:
            self._cart_page.checkout_modal_component.click_continue_button()
