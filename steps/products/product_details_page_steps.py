from pages.products.product_details_page import ProductDetailsPage
from tools.api.api_client import get_products_info


class ProductDetailsPageSteps:
    def __init__(self, product_details_page: ProductDetailsPage):
        self._product_details_page = product_details_page

    def open_page(self, product_id: int):
        self._product_details_page.open(product_id=product_id)
        self._product_details_page.check_product_image()

    def is_open_page(self, product_id: int):
        self._product_details_page.is_open(product_id=product_id)
        self._product_details_page.check_product_image()

    def add_product_to_cart(self, quantity: int = 1, redirect_to_cart_page: bool = False):
        self._product_details_page.product_information_component.fill_fields(quantity=quantity)
        self._product_details_page.product_information_component.click_add_to_cart_button()

        if redirect_to_cart_page:
            self._product_details_page.added_to_cart_modal_component.click_navigation_link()
        else:
            self._product_details_page.added_to_cart_modal_component.click_continue_button()

    def write_and_submit_review(self, name: str, email: str, review: str):
        self._product_details_page.product_review_form_component.fill_fields(name=name, email=email, review=review)
        self._product_details_page.product_review_form_component.click_submit()
        self._product_details_page.product_review_form_component.check_thank_you_alert()

    def verify_product_details_displayed(
            self,
            product_id,
            availability: str = ' In Stock',
            condition: str = ' New'
    ):
        product_info = get_products_info([product_id])[0]
        self._product_details_page.product_information_component.check_product_name_title(name=product_info['name'])
        self._product_details_page.product_information_component.check_category_text(
            category=product_info['category']['usertype']['usertype'] + ' > ' + product_info['category']['category']
        )
        self._product_details_page.product_information_component.check_price_text(
            price=int(product_info['price'].split()[1])
        )
        self._product_details_page.product_information_component.check_availability_text(availability=availability)
        self._product_details_page.product_information_component.check_condition_text(condition=condition)
        self._product_details_page.product_information_component.check_brand_text(brand=product_info['brand'])
