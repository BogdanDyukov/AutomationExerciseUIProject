from pages.authentication.signup_or_login_page import SignupOrLoginPage


class SignupOrLoginPageSteps:
    def __init__(self, signup_or_login_page: SignupOrLoginPage):
        self._signup_or_login_page = signup_or_login_page

    def open_page(self):
        self._signup_or_login_page.open()
        self._signup_or_login_page.login_form_component.check_title()
        self._signup_or_login_page.signup_form_component.check_title()

    def is_open_page(self):
        self._signup_or_login_page.is_open()
        self._signup_or_login_page.login_form_component.check_title()
        self._signup_or_login_page.signup_form_component.check_title()

    def login_to_account(self, email: str, password: str):
        self._signup_or_login_page.login_form_component.fill_fields(email=email, password=password)
        self._signup_or_login_page.login_form_component.click_login_button()

    def signup_new_account(self, name: str, email: str):
        self._signup_or_login_page.signup_form_component.fill_fields(name=name, email=email)
        self._signup_or_login_page.signup_form_component.click_signup_button()

    def verify_error_login_display(self):
        self._signup_or_login_page.login_form_component.check_incorrect_inputs_alert()

    def verify_error_signup_display(self):
        self._signup_or_login_page.signup_form_component.check_incorrect_inputs_alert()
