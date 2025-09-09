from models.test_user import TestUser
from pages.home_page import HomePage
from pages.authentication.signup_or_login_page import SignupOrLoginPage
from steps.home_page_steps import HomePageSteps
from steps.authentication.signup_or_login_page_steps import SignupOrLoginPageSteps


class TestAuthorization:
    def test_successful_authorization(
            self,
            home_page: HomePage,
            signup_or_login_page: SignupOrLoginPage,
            authorized_test_user: TestUser
    ):
        home_page.open()
        home_page.navbar_component.check_logo_link()
        home_page.navbar_component.click_signup_or_login_link()

        signup_or_login_page.is_open()
        signup_or_login_page.login_form_component.check_title()
        signup_or_login_page.login_form_component.fill_fields(
            email=authorized_test_user.account_information.email,
            password=authorized_test_user.account_information.password
        )
        signup_or_login_page.login_form_component.click_login_button()

        home_page.is_open()
        home_page.navbar_component.check_logged_in_user_text(authorized_test_user.account_information.name)

    def test_wrong_email_and_password_authorization(self, signup_or_login_page: SignupOrLoginPage):
        signup_or_login_page.open()
        signup_or_login_page.login_form_component.check_title()
        signup_or_login_page.login_form_component.fill_fields(
            email='incorrect.email@gmail.com',
            password='incorrect.password'
        )
        signup_or_login_page.login_form_component.click_login_button()
        signup_or_login_page.login_form_component.check_incorrect_inputs_alert()

    def test_successful_logout_user(
            self,
            home_page: HomePage,
            signup_or_login_page: SignupOrLoginPage,
            authorized_test_user: TestUser
    ):
        signup_or_login_page.open()
        signup_or_login_page.login_form_component.check_title()
        signup_or_login_page.login_form_component.fill_fields(
            email=authorized_test_user.account_information.email,
            password=authorized_test_user.account_information.password
        )
        signup_or_login_page.login_form_component.click_login_button()

        home_page.is_open()
        home_page.navbar_component.check_logged_in_user_text(authorized_test_user.account_information.name)
        home_page.navbar_component.click_logout_link()

        signup_or_login_page.is_open()

    def test_successful_authorization_2(
            self,
            home_page_steps: HomePageSteps,
            signup_or_login_page_steps: SignupOrLoginPageSteps,
            authorized_test_user: TestUser
    ):
        home_page_steps.open_page()
        home_page_steps.navbar.go_signup_or_login()

        signup_or_login_page_steps.is_open_page()
        signup_or_login_page_steps.login_to_account(
            email=authorized_test_user.account_information.email,
            password=authorized_test_user.account_information.password
        )

        home_page_steps.is_open_page()
        home_page_steps.navbar.verify_user_logged_in(username=authorized_test_user.account_information.name)

    def test_wrong_email_and_password_authorization_2(self, login_page_steps: SignupOrLoginPageSteps):
        login_page_steps.open_page()
        login_page_steps.login_to_account(
            email='incorrect.email@gmail.com',
            password='incorrect.password'
        )
        login_page_steps.verify_error_login_display()

    def test_successful_logout_user_2(
            self,
            home_page_steps: HomePageSteps,
            signup_or_login_page_steps: SignupOrLoginPageSteps,
            authorized_test_user: TestUser
    ):
        signup_or_login_page_steps.open_page()
        signup_or_login_page_steps.login_to_account(
            email=authorized_test_user.account_information.email,
            password=authorized_test_user.account_information.password
        )

        home_page_steps.is_open_page()
        home_page_steps.navbar.verify_user_logged_in(username=authorized_test_user.account_information.name)
        home_page_steps.navbar.go_logout()

        signup_or_login_page_steps.is_open_page()
