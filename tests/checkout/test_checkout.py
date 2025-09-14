import allure
import pytest

from config.settings import settings
from models.test_user import TestUser
from steps.authentication.account_created_page_steps import AccountCreatedPageSteps
from steps.cart.cart_page_steps import CartPageSteps
from steps.checkout.checkout_page_steps import CheckoutPageSteps
from steps.home_page_steps import HomePageSteps
from steps.checkout.payment_done_page_steps import PaymentDonePageSteps
from steps.checkout.payment_page_steps import PaymentPageSteps
from steps.authentication.signup_or_login_page_steps import SignupOrLoginPageSteps
from steps.authentication.signup_page_steps import SignupPageSteps
from tools.allure.epics import AllureEpic
from tools.allure.features import AllureFeature
from tools.allure.stories import AllureStory


@pytest.mark.regression
@pytest.mark.checkout
@allure.epic(AllureEpic.ORDER_PROCESSING)
@allure.feature(AllureFeature.CHECKOUT)
@allure.parent_suite(AllureEpic.ORDER_PROCESSING)
@allure.suite(AllureFeature.CHECKOUT)
class TestCheckout:
    @pytest.mark.parametrize('added_product_ids', [[1, 2]])
    @allure.story(AllureStory.SUCCESSFUL_CHECKOUT)
    @allure.sub_suite(AllureStory.SUCCESSFUL_CHECKOUT)
    @allure.title('Checkout with products with id: {added_product_ids}')
    @allure.severity(allure.severity_level.CRITICAL)
    def test_successful_checkout(
            self,
            home_page_steps_with_state: HomePageSteps,
            cart_page_steps_with_state: CartPageSteps,
            checkout_page_steps_with_state: CheckoutPageSteps,
            payment_page_steps_with_state: PaymentPageSteps,
            payment_done_page_steps_with_state: PaymentDonePageSteps,
            added_product_ids: list[int]
    ):
        home_page_steps_with_state.open_page()
        home_page_steps_with_state.add_products_to_cart(product_ids=added_product_ids, redirect_to_cart_page=True)

        cart_page_steps_with_state.is_open_page()
        cart_page_steps_with_state.proceed_to_checkout()

        checkout_page_steps_with_state.is_open_page()
        total_amount = checkout_page_steps_with_state.verify_order(product_ids_in_order=added_product_ids)
        checkout_page_steps_with_state.proceed_to_order_payment()

        payment_page_steps_with_state.is_open_page()
        payment_page_steps_with_state.enter_payment_information_and_confirm_order(payment_card_info=settings.payment_card_info)

        payment_done_page_steps_with_state.is_open_page(total_amount=total_amount)
        payment_done_page_steps_with_state.confirm_notification()

    @pytest.mark.parametrize('added_product_ids', [[1, 2]])
    @allure.story(AllureStory.CHECKOUT_WITH_REGISTRATION)
    @allure.title('Registration while checkout with products with id: {added_product_ids}')
    @allure.severity(allure.severity_level.NORMAL)
    def test_register_while_checkout(
            self,
            home_page_steps: HomePageSteps,
            cart_page_steps: CartPageSteps,
            signup_or_login_page_steps: SignupOrLoginPageSteps,
            signup_page_steps: SignupPageSteps,
            account_created_page_steps: AccountCreatedPageSteps,
            checkout_page_steps: CheckoutPageSteps,
            payment_page_steps: PaymentPageSteps,
            payment_done_page_steps: PaymentDonePageSteps,
            new_test_user: TestUser,
            added_product_ids: list[int]
    ):
        home_page_steps.open_page()
        home_page_steps.add_products_to_cart(product_ids=added_product_ids, redirect_to_cart_page=True)

        cart_page_steps.is_open_page()
        cart_page_steps.try_proceed_to_checkout_without_logging(redirect_to_signup_or_login_page=True)

        signup_or_login_page_steps.is_open_page()
        signup_or_login_page_steps.signup_new_account(
            name=new_test_user.account_information.name,
            email=new_test_user.account_information.email
        )
        signup_page_steps.is_open_page()
        signup_page_steps.enter_account_and_address_information_and_create_account(
            new_test_user=new_test_user,
            newsletter_flag=True,
            special_offers_flag=True
        )

        account_created_page_steps.is_open_page()
        account_created_page_steps.confirm_notification()

        home_page_steps.is_open_page()
        home_page_steps.navbar.verify_user_logged_in(new_test_user.account_information.name)
        home_page_steps.navbar.go_cart()

        cart_page_steps.is_open_page()
        cart_page_steps.proceed_to_checkout()

        checkout_page_steps.is_open_page()
        checkout_page_steps.verify_address(new_test_user)
        total_amount = checkout_page_steps.verify_order(product_ids_in_order=added_product_ids)
        checkout_page_steps.proceed_to_order_payment()

        payment_page_steps.is_open_page()
        payment_page_steps.enter_payment_information_and_confirm_order(payment_card_info=settings.payment_card_info)

        payment_done_page_steps.is_open_page(total_amount=total_amount)
        payment_done_page_steps.confirm_notification()

    @pytest.mark.parametrize('added_product_ids', [[1, 2]])
    @allure.story(AllureStory.CHECKOUT_AFTER_LOGIN)
    @allure.title('Login before checkout with products with id: {added_product_ids}')
    @allure.severity(allure.severity_level.NORMAL)
    def test_login_before_checkout(
            self,
            home_page_steps: HomePageSteps,
            cart_page_steps: CartPageSteps,
            signup_or_login_page_steps: SignupOrLoginPageSteps,
            checkout_page_steps: CheckoutPageSteps,
            payment_page_steps: PaymentPageSteps,
            payment_done_page_steps: PaymentDonePageSteps,
            authorized_test_user: TestUser,
            added_product_ids: list[int]
    ):
        signup_or_login_page_steps.open_page()
        signup_or_login_page_steps.login_to_account(
            email=authorized_test_user.account_information.email,
            password=authorized_test_user.account_information.password
        )
        home_page_steps.is_open_page()
        home_page_steps.navbar.verify_user_logged_in(authorized_test_user.account_information.name)
        home_page_steps.add_products_to_cart(product_ids=added_product_ids, redirect_to_cart_page=True)

        cart_page_steps.is_open_page()
        cart_page_steps.proceed_to_checkout()

        checkout_page_steps.is_open_page()
        checkout_page_steps.verify_address(test_user=authorized_test_user)
        total_amount = checkout_page_steps.verify_order(product_ids_in_order=added_product_ids)
        checkout_page_steps.proceed_to_order_payment()

        payment_page_steps.is_open_page()
        payment_page_steps.enter_payment_information_and_confirm_order(payment_card_info=settings.payment_card_info)

        payment_done_page_steps.is_open_page(total_amount=total_amount)
        payment_done_page_steps.confirm_notification()

    @pytest.mark.parametrize('added_product_ids', [[1, 5]])
    @allure.story(AllureStory.DOWNLOAD_INVOICE_AFTER_CHECKOUT)
    @allure.title('Checking the download invoice after checkout with products with an id: {added_product_ids}')
    @allure.severity(allure.severity_level.CRITICAL)
    def test_download_invoice_after_purchase_order(
            self,
            home_page_steps: HomePageSteps,
            cart_page_steps: CartPageSteps,
            signup_or_login_page_steps: SignupOrLoginPageSteps,
            checkout_page_steps: CheckoutPageSteps,
            payment_page_steps: PaymentPageSteps,
            payment_done_page_steps: PaymentDonePageSteps,
            authorized_test_user: TestUser,
            added_product_ids: list[int]
    ):
        signup_or_login_page_steps.open_page()
        signup_or_login_page_steps.login_to_account(
            email=authorized_test_user.account_information.email,
            password=authorized_test_user.account_information.password
        )

        home_page_steps.is_open_page()
        home_page_steps.navbar.verify_user_logged_in(authorized_test_user.account_information.name)
        home_page_steps.add_products_to_cart(product_ids=added_product_ids, redirect_to_cart_page=True)

        cart_page_steps.is_open_page()
        cart_page_steps.proceed_to_checkout()

        checkout_page_steps.is_open_page()
        checkout_page_steps.verify_address(test_user=authorized_test_user)
        total_amount = checkout_page_steps.verify_order(product_ids_in_order=added_product_ids)
        checkout_page_steps.proceed_to_order_payment()

        payment_page_steps.is_open_page()
        payment_page_steps.enter_payment_information_and_confirm_order(payment_card_info=settings.payment_card_info)

        payment_done_page_steps.is_open_page(total_amount=total_amount)
        payment_done_page_steps.download_invoice(file_path=settings.downloads_dir)
        payment_done_page_steps.confirm_notification()
