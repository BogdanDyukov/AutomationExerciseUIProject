from data.test_users import authorized_test_user
from pages.home_page import HomePage
from pages.authentication.signup_or_login_page import SignupOrLoginPage


class TestAuthorization:
    def test_successful_authorization(self, home_page: HomePage, signup_or_login_page: SignupOrLoginPage):
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
        home_page.navbar_component.check_logged_in_user_label(authorized_test_user.account_information.name)

    def test_wrong_email_and_password_authorization(self, signup_or_login_page: SignupOrLoginPage):
        signup_or_login_page.open()
        signup_or_login_page.login_form_component.check_title()
        signup_or_login_page.login_form_component.fill_fields(
            email='incorrect.email@gmail.com',
            password='incorrect.password'
        )
        signup_or_login_page.login_form_component.click_login_button()
        signup_or_login_page.login_form_component.check_incorrect_inputs_text()

    def test_successful_logout_user(self, home_page: HomePage, signup_or_login_page: SignupOrLoginPage):
        signup_or_login_page.open()
        signup_or_login_page.login_form_component.check_title()
        signup_or_login_page.login_form_component.fill_fields(
            email=authorized_test_user.account_information.email,
            password=authorized_test_user.account_information.password
        )
        signup_or_login_page.login_form_component.click_login_button()

        home_page.is_open()
        home_page.navbar_component.check_logged_in_user_label(authorized_test_user.account_information.name)
        home_page.navbar_component.click_logout_link()

        signup_or_login_page.is_open()
