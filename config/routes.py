from enum import Enum


class AppRoute(str, Enum):
    HOME = './'
    PRODUCTS = './products'
    # PRODUCTS_SEARCH = '/products?search={search_query}'
    PRODUCT_DETAILS = '/product_details/{product_id}'
    CART = './view_cart'
    SIGNUP_OR_LOGIN = './login'
    SIGNUP = './signup'
    ACCOUNT_CREATED = "./account_created"
    ACCOUNT_DELETED = "./delete_account"
    TEST_CASES = "./test_cases"
    CONTACT_US = "./contact_us"
