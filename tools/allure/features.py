from enum import Enum


class AllureFeature(str, Enum):
    AUTHORIZATION = 'Authorization'
    LOGOUT = 'Logout'
    REGISTRATION = 'Registration'

    CART_STATE = "Cart State"
    CART_OPERATIONS = "Cart operations"

    CHECKOUT = 'Checkout'

    CONTACT = 'Contact'
    SUBSCRIPTION = 'Subscription'

    PRODUCT_LISTING = "Product Listing"
    PRODUCT_DETAILS = "Product Details"
    PRODUCT_REVIEW = "Product Review"
    PRODUCT_SEARCH = "Product Search"

    SCROLL = "Scroll"
