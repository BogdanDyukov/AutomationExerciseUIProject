from data.test_users import new_test_user, authorized_test_user
from pages.notifications.account_created_page import AccountCreatedPage
from pages.notifications.account_deleted_page import AccountDeletedPage
from pages.home_page import HomePage
from pages.authentication.signup_or_login_page import SignupOrLoginPage
from pages.authentication.signup_page import SignupPage


class TestRegistration:
    def test_successful_registration(
            self,
            home_page: HomePage,
            signup_or_login_page: SignupOrLoginPage,
            signup_page: SignupPage,
            account_created_page: AccountCreatedPage,
            account_deleted_page: AccountDeletedPage
    ):
        home_page.open()
        home_page.navbar_component.check_logo_link()
        home_page.navbar_component.click_signup_or_login_link()

        signup_or_login_page.is_open()
        signup_or_login_page.signup_form_component.check_title()
        signup_or_login_page.signup_form_component.fill_fields(
            name=new_test_user.account_information.name,
            email=new_test_user.account_information.email
        )
        signup_or_login_page.signup_form_component.click_signup_button()

        signup_page.is_open()
        signup_page.account_information_component.check_title()
        signup_page.account_information_component.fill_fields(
            gender=new_test_user.account_information.title,
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
        account_created_page.notification_component.check_title()
        account_created_page.notification_component.click_continue_button()

        home_page.is_open()
        home_page.navbar_component.check_logged_in_user_label(new_test_user.account_information.name)
        home_page.navbar_component.click_delete_account_link()

        account_deleted_page.is_open()
        account_deleted_page.notification_component.check_title()
        account_deleted_page.notification_component.click_continue_button()

    def test_register_user_with_existing_email(self, signup_or_login_page: SignupOrLoginPage):
        signup_or_login_page.open()
        signup_or_login_page.signup_form_component.check_title()
        signup_or_login_page.signup_form_component.fill_fields(
            name=authorized_test_user.account_information.name,
            email=authorized_test_user.account_information.email
        )
        signup_or_login_page.signup_form_component.click_signup_button()
        signup_or_login_page.signup_form_component.check_incorrect_inputs_text()
