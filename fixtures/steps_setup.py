import pytest

from pages.authentication.account_created_page import AccountCreatedPage
from pages.authentication.account_deleted_page import AccountDeletedPage
from pages.authentication.signup_or_login_page import SignupOrLoginPage
from pages.authentication.signup_page import SignupPage
from pages.cart.cart_page import CartPage
from pages.checkout.checkout_page import CheckoutPage
from pages.checkout.payment_done_page import PaymentDonePage
from pages.checkout.payment_page import PaymentPage
from pages.home_page import HomePage
from pages.products.product_details_page import ProductDetailsPage
from pages.products.products_page import ProductsPage
from steps.authentication.account_created_page_steps import AccountCreatedPageSteps
from steps.authentication.account_deleted_page_steps import AccountDeletedPageSteps
from steps.cart.cart_page_steps import CartPageSteps
from steps.checkout.checkout_page_steps import CheckoutPageSteps
from steps.home_page_steps import HomePageSteps
from steps.checkout.payment_done_page_steps import PaymentDonePageSteps
from steps.checkout.payment_page_steps import PaymentPageSteps
from steps.authentication.signup_or_login_page_steps import SignupOrLoginPageSteps
from steps.products.product_details_page_steps import ProductDetailsPageSteps
from steps.products.products_page_steps import ProductsPageSteps
from steps.authentication.signup_page_steps import SignupPageSteps


@pytest.fixture
def home_page_steps(home_page: HomePage) -> HomePageSteps:
    return HomePageSteps(home_page=home_page)


@pytest.fixture
def home_page_steps_with_state(home_page_with_state: HomePage) -> HomePageSteps:
    return HomePageSteps(home_page=home_page_with_state)


@pytest.fixture
def products_page_steps(products_page: ProductsPage) -> ProductsPageSteps:
    return ProductsPageSteps(products_page=products_page)


@pytest.fixture
def product_details_page_steps(product_details_page: ProductDetailsPage) -> ProductDetailsPageSteps:
    return ProductDetailsPageSteps(product_details_page=product_details_page)


@pytest.fixture
def cart_page_steps(cart_page: CartPage) -> CartPageSteps:
    return CartPageSteps(cart_page=cart_page)


@pytest.fixture
def cart_page_steps_with_state(cart_page_with_state: CartPage) -> CartPageSteps:
    return CartPageSteps(cart_page=cart_page_with_state)


@pytest.fixture
def signup_or_login_page_steps(signup_or_login_page: SignupOrLoginPage) -> SignupOrLoginPageSteps:
    return SignupOrLoginPageSteps(signup_or_login_page=signup_or_login_page)


@pytest.fixture
def signup_page_steps(signup_page: SignupPage) -> SignupPageSteps:
    return SignupPageSteps(signup_page=signup_page)


@pytest.fixture
def account_created_page_steps(account_created_page: AccountCreatedPage) -> AccountCreatedPageSteps:
    return AccountCreatedPageSteps(account_created_page=account_created_page)


@pytest.fixture
def account_deleted_page_steps(account_deleted_page: AccountDeletedPage) -> AccountDeletedPageSteps:
    return AccountDeletedPageSteps(account_deleted_page=account_deleted_page)


@pytest.fixture
def checkout_page_steps(checkout_page: CheckoutPage) -> CheckoutPageSteps:
    return CheckoutPageSteps(checkout_page=checkout_page)


@pytest.fixture
def checkout_page_steps_with_state(checkout_page_with_state: CheckoutPage) -> CheckoutPageSteps:
    return CheckoutPageSteps(checkout_page=checkout_page_with_state)


@pytest.fixture
def payment_page_steps(payment_page: PaymentPage) -> PaymentPageSteps:
    return PaymentPageSteps(payment_page=payment_page)


@pytest.fixture
def payment_page_steps_with_state(payment_page_with_state: PaymentPage) -> PaymentPageSteps:
    return PaymentPageSteps(payment_page=payment_page_with_state)


@pytest.fixture
def payment_done_page_steps(payment_done_page: PaymentDonePage) -> PaymentDonePageSteps:
    return PaymentDonePageSteps(payment_done_page=payment_done_page)


@pytest.fixture
def payment_done_page_steps_with_state(payment_done_page_with_state: PaymentDonePage) -> PaymentDonePageSteps:
    return PaymentDonePageSteps(payment_done_page=payment_done_page_with_state)
