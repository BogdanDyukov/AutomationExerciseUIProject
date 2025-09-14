import allure

from models.test_user import TestUser
from pages.checkout.checkout_page import CheckoutPage
from tools.api.products import get_products_info


class CheckoutPageSteps:
    def __init__(self, checkout_page: CheckoutPage):
        self._checkout_page = checkout_page

    # @allure.step('Open checkout page')
    def open_page(self):
        self._checkout_page.open()
        self._checkout_page.breadcrumb_component.check_breadcrumb_current_item()
        self._checkout_page.breadcrumb_component.check_breadcrumb_home_item_link()

    # @allure.step('Check that the checkout page is open')
    def is_open_page(self):
        self._checkout_page.is_open()
        self._checkout_page.breadcrumb_component.check_breadcrumb_current_item()
        self._checkout_page.breadcrumb_component.check_breadcrumb_home_item_link()

    # @allure.step('Check delivery address')
    def verify_address(self, test_user: TestUser):
        self._checkout_page.address_delivery_component.check_title()
        self._checkout_page.address_delivery_component.check_gender_and_firstname_and_lastname_text(
            test_user.address_information.firstname,
            test_user.address_information.lastname,
            test_user.account_information.gender
        )
        self._checkout_page.address_delivery_component.check_company_text(test_user.address_information.company)
        self._checkout_page.address_delivery_component.check_first_address_text(test_user.address_information.address1)
        self._checkout_page.address_delivery_component.check_second_address_text(test_user.address_information.address2)
        self._checkout_page.address_delivery_component.check_city_and_state_and_postcode_text(
            test_user.address_information.city,
            test_user.address_information.state,
            test_user.address_information.zipcode
        )
        self._checkout_page.address_delivery_component.check_country_text(test_user.address_information.country)
        self._checkout_page.address_delivery_component.check_mobile_number_text(
            test_user.address_information.mobile_number
        )

    # @allure.step('Check the correctness of the order')
    def verify_order(self, product_ids_in_order: list[int]) -> int:
        assert (len(self._checkout_page.table_cart_with_total_row_component.get_product_ids())
                == len(set(product_ids_in_order))), 'The number of items in the order does not match the transmitted'

        with allure.step('Get the details for each product in the order'):
            products_info = get_products_info(product_ids_in_order)

        total_amount = 0

        for product_info in products_info:
            product_id = int(product_info['id'])
            product_price = int(product_info['price'].split()[1])
            product_quantity = product_ids_in_order.count(product_id)
            product_total_price = product_price * product_quantity

            self._checkout_page.table_cart_with_total_row_component.product_row_component.check_name_link(
                product_id=product_id,
                name=product_info['name']
            )
            self._checkout_page.table_cart_with_total_row_component.product_row_component.check_category_text(
                product_id=product_id,
                category=product_info['category']['usertype']['usertype'] + ' > ' + product_info['category']['category']
            )

            total_amount += product_total_price

        self._checkout_page.table_cart_with_total_row_component.total_row_component.check_total_price_text(
            total_price=total_amount
        )

        return total_amount

    # @allure.step('Proceed to order payment')
    def proceed_to_order_payment(self):
        self._checkout_page.click_place_order_button()
