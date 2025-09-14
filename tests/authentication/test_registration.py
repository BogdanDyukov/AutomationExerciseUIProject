import allure
import pytest

from models.test_user import TestUser
from steps.authentication.account_created_page_steps import AccountCreatedPageSteps
from steps.authentication.account_deleted_page_steps import AccountDeletedPageSteps
from steps.home_page_steps import HomePageSteps
from steps.authentication.signup_or_login_page_steps import SignupOrLoginPageSteps
from steps.authentication.signup_page_steps import SignupPageSteps
from tools.allure.epics import AllureEpic
from tools.allure.features import AllureFeature
from tools.allure.stories import AllureStory


@pytest.mark.regression
@pytest.mark.registration
@allure.epic(AllureEpic.USER_MANAGEMENT)
@allure.feature(AllureFeature.REGISTRATION)
@allure.parent_suite(AllureEpic.USER_MANAGEMENT)
@allure.suite(AllureFeature.REGISTRATION)
class TestRegistration:
    @allure.story(AllureStory.SUCCESSFUL_REGISTRATION)
    @allure.sub_suite(AllureStory.SUCCESSFUL_REGISTRATION)
    @allure.title("Registration with correct data")
    @allure.severity(allure.severity_level.CRITICAL)
    def test_successful_registration(
            self,
            home_page_steps: HomePageSteps,
            signup_or_login_page_steps: SignupOrLoginPageSteps,
            signup_page_steps: SignupPageSteps,
            account_created_page_steps: AccountCreatedPageSteps,
            account_deleted_page_steps: AccountDeletedPageSteps,
            new_test_user: TestUser
    ):
        home_page_steps.open_page()
        home_page_steps.navbar.go_signup_or_login()

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

        account_created_page_steps.open_page()
        account_created_page_steps.confirm_notification()

        home_page_steps.is_open_page()
        home_page_steps.navbar.verify_user_logged_in(username=new_test_user.account_information.name)
        home_page_steps.navbar.go_delete_account()

        account_deleted_page_steps.is_open_page()
        account_deleted_page_steps.confirm_notification()

    @allure.story(AllureStory.FAILED_REGISTRATION)
    @allure.sub_suite(AllureStory.FAILED_REGISTRATION)
    @allure.title("Registration with existing email")
    @allure.severity(allure.severity_level.CRITICAL)
    def test_register_user_with_existing_email(
            self,
            signup_or_login_page_steps: SignupOrLoginPageSteps,
            authorized_test_user: TestUser
    ):
        signup_or_login_page_steps.open_page()
        signup_or_login_page_steps.signup_new_account(
            name=authorized_test_user.account_information.name,
            email=authorized_test_user.account_information.email
        )
        signup_or_login_page_steps.verify_error_signup_display()
