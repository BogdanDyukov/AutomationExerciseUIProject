import pytest
from playwright.sync_api import Page

from pages.authentication.account_created_page import AccountCreatedPage
from pages.authentication.account_deleted_page import AccountDeletedPage
from pages.cart.cart_page import CartPage
from pages.checkout.checkout_page import CheckoutPage
from pages.contact_us.contact_us_page import ContactUsPage
from pages.home_page import HomePage
from pages.checkout.payment_done_page import PaymentDonePage
from pages.checkout.payment_page import PaymentPage
from pages.products.product_details_page import ProductDetailsPage
from pages.products.products_page import ProductsPage
from pages.authentication.signup_or_login_page import SignupOrLoginPage
from pages.authentication.signup_page import SignupPage
from pages.cases.test_cases_page import TestCasesPage
from config.routes import AppRoute


@pytest.fixture
def home_page(page: Page) -> HomePage:
    return HomePage(page=page, path=AppRoute.HOME)


@pytest.fixture
def home_page_with_state(page_with_state: Page) -> HomePage:
    return HomePage(page=page_with_state, path=AppRoute.HOME)


@pytest.fixture
def products_page(page: Page) -> ProductsPage:
    return ProductsPage(page=page, path=AppRoute.PRODUCTS)


@pytest.fixture
def product_details_page(page: Page) -> ProductDetailsPage:
    return ProductDetailsPage(page=page, path=AppRoute.PRODUCT_DETAILS)


@pytest.fixture
def cart_page(page: Page) -> CartPage:
    return CartPage(page=page, path=AppRoute.CART)


@pytest.fixture
def cart_page_with_state(page_with_state: Page) -> CartPage:
    return CartPage(page=page_with_state, path=AppRoute.CART)


@pytest.fixture
def checkout_page(page: Page) -> CheckoutPage:
    return CheckoutPage(page=page, path=AppRoute.CHECKOUT)


@pytest.fixture
def checkout_page_with_state(page_with_state: Page) -> CheckoutPage:
    return CheckoutPage(page=page_with_state, path=AppRoute.CHECKOUT)


@pytest.fixture
def payment_page(page: Page) -> PaymentPage:
    return PaymentPage(page=page, path=AppRoute.PAYMENT)


@pytest.fixture
def payment_page_with_state(page_with_state: Page) -> PaymentPage:
    return PaymentPage(page=page_with_state, path=AppRoute.PAYMENT)


@pytest.fixture
def payment_done_page(page: Page) -> PaymentDonePage:
    return PaymentDonePage(page=page, path=AppRoute.PAYMENT_DONE)


@pytest.fixture
def payment_done_page_with_state(page_with_state: Page) -> PaymentDonePage:
    return PaymentDonePage(page=page_with_state, path=AppRoute.PAYMENT_DONE)


@pytest.fixture
def signup_or_login_page(page: Page) -> SignupOrLoginPage:
    return SignupOrLoginPage(page=page, path=AppRoute.SIGNUP_OR_LOGIN)


@pytest.fixture
def signup_or_login_page_with_state(page_with_state: Page) -> SignupOrLoginPage:
    return SignupOrLoginPage(page=page_with_state, path=AppRoute.SIGNUP_OR_LOGIN)


@pytest.fixture
def signup_page(page: Page) -> SignupPage:
    return SignupPage(page=page, path=AppRoute.SIGNUP)


@pytest.fixture
def account_created_page(page: Page) -> AccountCreatedPage:
    return AccountCreatedPage(page=page, path=AppRoute.ACCOUNT_CREATED)


@pytest.fixture
def account_deleted_page(page: Page) -> AccountDeletedPage:
    return AccountDeletedPage(page=page, path=AppRoute.ACCOUNT_DELETED)


@pytest.fixture
def test_cases_page(page: Page) -> TestCasesPage:
    return TestCasesPage(page=page, path=AppRoute.TEST_CASES)


@pytest.fixture
def contact_us_page(page: Page) -> ContactUsPage:
    return ContactUsPage(page=page, path=AppRoute.CONTACT_US)


@pytest.fixture
def contact_us_page_with_state(page_with_state: Page) -> ContactUsPage:
    return ContactUsPage(page=page_with_state, path=AppRoute.CONTACT_US)
