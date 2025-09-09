from models.test_user import TestUser
from pages.authentication.signup_page import SignupPage


class SignupPageSteps:
    def __init__(self, signup_page: SignupPage):
        self._signup_page = signup_page

    def open_page(self):
        self._signup_page.open()
        self._signup_page.account_information_component.check_title()

    def is_open_page(self):
        self._signup_page.is_open()
        self._signup_page.account_information_component.check_title()

    def enter_account_and_address_information_and_create_account(
            self,
            new_test_user: TestUser,
            newsletter_flag=True,
            special_offers_flag=True
    ):
        self._signup_page.account_information_component.fill_fields(
            gender=new_test_user.account_information.gender,
            name=new_test_user.account_information.name,
            password=new_test_user.account_information.password,
            day_value=new_test_user.date_of_birth.birth_date,
            month_value=new_test_user.date_of_birth.birth_month,
            year_value=new_test_user.date_of_birth.birth_year,
            newsletter_flag=newsletter_flag,
            special_offers_flag=special_offers_flag
        )
        self._signup_page.address_information_component.fill_fields(
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
        self._signup_page.click_create_account_button()
