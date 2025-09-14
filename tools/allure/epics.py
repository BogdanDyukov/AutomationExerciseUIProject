from enum import Enum


class AllureEpic(str, Enum):
    USER_MANAGEMENT = 'User Management'

    SHOPPING_CART = 'Shopping cart'

    ORDER_PROCESSING = "Order Processing"

    INTERACTIONS = 'interactions'

    PRODUCT_CATALOG = "Product Catalog"

    NAVIGATION = "Navigation"
