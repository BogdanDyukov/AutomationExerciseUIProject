import pytest

from config.settings import settings
from models.test_user import TestUser
from pages.authentication.account_created_page import AccountCreatedPage
from pages.authentication.account_deleted_page import AccountDeletedPage
from pages.authentication.signup_or_login_page import SignupOrLoginPage
from pages.authentication.signup_page import SignupPage
from pages.cart.cart_page import CartPage
from pages.checkout.checkout_page import CheckoutPage
from pages.checkout.payment_done_page import PaymentDonePage
from pages.checkout.payment_page import PaymentPage
from pages.home_page import HomePage
from steps.authentication.account_created_page_steps import AccountCreatedPageSteps
from steps.cart.cart_page_steps import CartPageSteps
from steps.checkout.checkout_page_steps import CheckoutPageSteps
from steps.home_page_steps import HomePageSteps
from steps.checkout.payment_done_page_steps import PaymentDonePageSteps
from steps.checkout.payment_page_steps import PaymentPageSteps
from steps.authentication.signup_or_login_page_steps import SignupOrLoginPageSteps
from steps.authentication.signup_page_steps import SignupPageSteps


class TestCheckout:
    def test_register_while_checkout(
            self,
            home_page: HomePage,
            cart_page: CartPage,
            signup_or_login_page: SignupOrLoginPage,
            signup_page: SignupPage,
            account_created_page: AccountCreatedPage,
            checkout_page: CheckoutPage,
            payment_page: PaymentPage,
            payment_done_page: PaymentDonePage,
            account_deleted_page: AccountDeletedPage,
            new_test_user: TestUser
    ):
        home_page.open()
        home_page.navbar_component.check_logo_link()
        home_page.list_of_product_cards_component.product_card_component.click_add_to_cart_button(product_id=1)
        home_page.added_to_cart_modal_component.click_continue_button()
        home_page.list_of_product_cards_component.product_card_component.click_add_to_cart_button(product_id=5)
        home_page.added_to_cart_modal_component.click_navigation_link()

        cart_page.is_open()
        cart_page.click_proceed_to_checkout_button()
        cart_page.checkout_modal_component.check_title()
        cart_page.checkout_modal_component.click_navigation_link()

        signup_or_login_page.is_open()
        signup_or_login_page.signup_form_component.fill_fields(
            name=new_test_user.account_information.name,
            email=new_test_user.account_information.email
        )
        signup_or_login_page.signup_form_component.click_signup_button()

        signup_page.is_open()
        signup_page.account_information_component.fill_fields(
            gender=new_test_user.account_information.gender,
            name=new_test_user.account_information.name,
            password=new_test_user.account_information.password,
            day_value=new_test_user.date_of_birth.birth_date,
            month_value=new_test_user.date_of_birth.birth_month,
            year_value=new_test_user.date_of_birth.birth_year,
            newsletter_flag=True,
            special_offers_flag=True
        )
        signup_page.address_information_component.fill_fields(
            first_name=new_test_user.address_information.firstname,
            last_name=new_test_user.address_information.lastname,
            company=new_test_user.address_information.company,
            first_address=new_test_user.address_information.address1,
            second_address=new_test_user.address_information.address2,
            country_value=new_test_user.address_information.country,
            state=new_test_user.address_information.state,
            city=new_test_user.address_information.city,
            zipcode=new_test_user.address_information.zipcode,
            mobile_number=new_test_user.address_information.mobile_number
        )
        signup_page.click_create_account_button()

        account_created_page.is_open()
        account_created_page.notification_component.click_continue_button()

        home_page.is_open()
        home_page.navbar_component.check_logged_in_user_text(new_test_user.account_information.name)
        home_page.navbar_component.click_cart_link()

        cart_page.is_open()
        cart_page.click_proceed_to_checkout_button()

        checkout_page.is_open()
        checkout_page.address_delivery_component.check_all(
            first_name=new_test_user.address_information.firstname,
            last_name=new_test_user.address_information.lastname,
            gender=new_test_user.account_information.gender,
            company=new_test_user.address_information.company,
            first_address=new_test_user.address_information.address1,
            second_address=new_test_user.address_information.address2,
            country=new_test_user.address_information.country,
            state=new_test_user.address_information.state,
            city=new_test_user.address_information.city,
            postcode=new_test_user.address_information.zipcode,
            mobile_number=new_test_user.address_information.mobile_number
        )
        checkout_page.table_cart_with_total_row_component.product_row_component.check_product_name_link(
            product_id=1,
            name='Blue Top'
        )
        checkout_page.table_cart_with_total_row_component.product_row_component.check_product_name_link(
            product_id=5,
            name='Winter Top'
        )
        checkout_page.table_cart_with_total_row_component.total_row_component.check_total_price_text(total_price=1100)
        checkout_page.order_comment_component.fill_fields(message='Comment about my order')
        checkout_page.click_place_order_button()

        payment_page.is_open()
        payment_page.payment_form_component.fill_fields(
            card_name=settings.payment_card_info.name,
            card_number=settings.payment_card_info.number,
            cvc=str(settings.payment_card_info.cvc),
            expiry_month=settings.payment_card_info.expiry_month,
            expiry_year=str(settings.payment_card_info.expiry_year)
        )
        payment_page.payment_form_component.click_pay_button()

        payment_done_page.is_open(total_amount=1100)
        payment_done_page.order_notification_component.check_all()

    def test_login_before_checkout(
            self,
            home_page: HomePage,
            cart_page: CartPage,
            signup_or_login_page: SignupOrLoginPage,
            checkout_page: CheckoutPage,
            payment_page: PaymentPage,
            payment_done_page: PaymentDonePage,
            authorized_test_user: TestUser
    ):
        signup_or_login_page.open()
        signup_or_login_page.login_form_component.fill_fields(
            email=authorized_test_user.account_information.email,
            password=authorized_test_user.account_information.password
        )
        signup_or_login_page.login_form_component.click_login_button()

        home_page.is_open()
        home_page.navbar_component.check_logged_in_user_text(authorized_test_user.account_information.name)
        home_page.list_of_product_cards_component.product_card_component.click_add_to_cart_button(product_id=1)
        home_page.added_to_cart_modal_component.click_continue_button()
        home_page.list_of_product_cards_component.product_card_component.click_add_to_cart_button(product_id=5)
        home_page.added_to_cart_modal_component.click_navigation_link()

        cart_page.is_open()
        cart_page.click_proceed_to_checkout_button()

        checkout_page.is_open()
        checkout_page.address_delivery_component.check_all(
            first_name=authorized_test_user.address_information.firstname,
            last_name=authorized_test_user.address_information.lastname,
            gender=authorized_test_user.account_information.gender,
            company=authorized_test_user.address_information.company,
            first_address=authorized_test_user.address_information.address1,
            second_address=authorized_test_user.address_information.address2,
            country=authorized_test_user.address_information.country,
            state=authorized_test_user.address_information.state,
            city=authorized_test_user.address_information.city,
            postcode=authorized_test_user.address_information.zipcode,
            mobile_number=authorized_test_user.address_information.mobile_number
        )
        checkout_page.table_cart_with_total_row_component.product_row_component.check_product_name_link(
            product_id=1,
            name='Blue Top'
        )
        checkout_page.table_cart_with_total_row_component.product_row_component.check_product_name_link(
            product_id=5,
            name='Winter Top'
        )
        checkout_page.table_cart_with_total_row_component.total_row_component.check_total_price_text(total_price=1100)
        checkout_page.order_comment_component.fill_fields(message='Comment about my order')
        checkout_page.click_place_order_button()

        payment_page.is_open()
        payment_page.payment_form_component.fill_fields(
            card_name=settings.payment_card_info.name,
            card_number=settings.payment_card_info.number,
            cvc=str(settings.payment_card_info.cvc),
            expiry_month=settings.payment_card_info.expiry_month,
            expiry_year=str(settings.payment_card_info.expiry_year)
        )
        payment_page.payment_form_component.click_pay_button()

        payment_done_page.is_open(total_amount=1100)
        payment_done_page.order_notification_component.check_all()
        payment_done_page.order_notification_component.click_continue_button()

    def test_download_invoice_after_purchase_order(
            self,
            signup_or_login_page: SignupOrLoginPage,
            home_page: HomePage,
            cart_page: CartPage,
            checkout_page: CheckoutPage,
            payment_page: PaymentPage,
            payment_done_page: PaymentDonePage,
            authorized_test_user: TestUser
    ):
        signup_or_login_page.open()
        signup_or_login_page.login_form_component.fill_fields(
            email=authorized_test_user.account_information.email,
            password=authorized_test_user.account_information.password
        )
        signup_or_login_page.login_form_component.click_login_button()

        home_page.is_open()
        home_page.navbar_component.check_logged_in_user_text(authorized_test_user.account_information.name)
        home_page.list_of_product_cards_component.product_card_component.click_add_to_cart_button(
            product_id=1
        )
        home_page.added_to_cart_modal_component.click_continue_button()
        home_page.list_of_product_cards_component.product_card_component.click_add_to_cart_button(
            product_id=5
        )
        home_page.added_to_cart_modal_component.click_navigation_link()

        cart_page.is_open()
        cart_page.click_proceed_to_checkout_button()

        checkout_page.is_open()
        checkout_page.address_delivery_component.check_all(
            first_name=authorized_test_user.address_information.firstname,
            last_name=authorized_test_user.address_information.lastname,
            gender=authorized_test_user.account_information.gender,
            company=authorized_test_user.address_information.company,
            first_address=authorized_test_user.address_information.address1,
            second_address=authorized_test_user.address_information.address2,
            country=authorized_test_user.address_information.country,
            state=authorized_test_user.address_information.state,
            city=authorized_test_user.address_information.city,
            postcode=authorized_test_user.address_information.zipcode,
            mobile_number=authorized_test_user.address_information.mobile_number
        )
        checkout_page.table_cart_with_total_row_component.product_row_component.check_product_name_link(
            product_id=1,
            name='Blue Top'
        )
        checkout_page.table_cart_with_total_row_component.product_row_component.check_product_name_link(
            product_id=5,
            name='Winter Top'
        )
        checkout_page.table_cart_with_total_row_component.total_row_component.check_total_price_text(total_price=1100)
        checkout_page.order_comment_component.fill_fields(message='Comment about my order')
        checkout_page.click_place_order_button()

        payment_page.is_open()
        payment_page.payment_form_component.fill_fields(
            card_name=settings.payment_card_info.name,
            card_number=settings.payment_card_info.number,
            cvc=str(settings.payment_card_info.cvc),
            expiry_month=settings.payment_card_info.expiry_month,
            expiry_year=str(settings.payment_card_info.expiry_year)
        )
        payment_page.payment_form_component.click_pay_button()

        payment_done_page.is_open(total_amount=1100)
        payment_done_page.order_notification_component.check_all()

        payment_done_page.order_notification_component.download_invoice(file_path=settings.downloads_dir)

        payment_done_page.order_notification_component.click_continue_button()

    @pytest.mark.parametrize('added_product_ids', [[1, 2]])
    def test_register_while_checkout_2(
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
    def test_login_before_checkout_2(
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
    def test_download_invoice_after_purchase_order_2(
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
