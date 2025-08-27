import pytest
from playwright.sync_api import Page

from pages.notifications.account_created_page import AccountCreatedPage
from pages.notifications.account_deleted_page import AccountDeletedPage
from pages.cart.cart_page import CartPage
from pages.interactions.contact_us_page import ContactUsPage
from pages.home_page import HomePage
from pages.products.product_details_page import ProductDetailsPage
from pages.products.products_page import ProductsPage
from pages.authentication.signup_or_login_page import SignupOrLoginPage
from pages.authentication.signup_page import SignupPage
from pages.cases.test_cases_page import TestCasesPage
from config.routes import AppRoute


@pytest.fixture
def home_page(chromium_page: Page) -> HomePage:
    return HomePage(page=chromium_page, path=AppRoute.HOME)


@pytest.fixture
def home_page_with_state(chromium_page_with_state: Page) -> HomePage:
    return HomePage(page=chromium_page_with_state, path=AppRoute.HOME)


@pytest.fixture
def products_page(chromium_page: Page) -> ProductsPage:
    return ProductsPage(page=chromium_page, path=AppRoute.PRODUCTS)


@pytest.fixture
def product_details_page(chromium_page: Page) -> ProductDetailsPage:
    return ProductDetailsPage(page=chromium_page, path=AppRoute.PRODUCT_DETAILS)


@pytest.fixture
def cart_page(chromium_page: Page) -> CartPage:
    return CartPage(page=chromium_page, path=AppRoute.CART)


@pytest.fixture
def signup_or_login_page(chromium_page: Page) -> SignupOrLoginPage:
    return SignupOrLoginPage(page=chromium_page, path=AppRoute.SIGNUP_OR_LOGIN)


@pytest.fixture
def signup_or_login_page_with_state(chromium_page_with_state: Page) -> SignupOrLoginPage:
    return SignupOrLoginPage(page=chromium_page_with_state, path=AppRoute.SIGNUP_OR_LOGIN)


@pytest.fixture
def signup_page(chromium_page: Page) -> SignupPage:
    return SignupPage(page=chromium_page, path=AppRoute.SIGNUP)


@pytest.fixture
def account_created_page(chromium_page: Page) -> AccountCreatedPage:
    return AccountCreatedPage(page=chromium_page, path=AppRoute.ACCOUNT_CREATED)


@pytest.fixture
def account_deleted_page(chromium_page: Page) -> AccountDeletedPage:
    return AccountDeletedPage(page=chromium_page, path=AppRoute.ACCOUNT_DELETED)


@pytest.fixture
def test_cases_page(chromium_page: Page) -> TestCasesPage:
    return TestCasesPage(page=chromium_page, path=AppRoute.TEST_CASES)


@pytest.fixture
def contact_us_page(chromium_page: Page) -> ContactUsPage:
    return ContactUsPage(page=chromium_page, path=AppRoute.CONTACT_US)
