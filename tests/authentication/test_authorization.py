import allure
import pytest

from models.test_user import TestUser
from steps.home_page_steps import HomePageSteps
from steps.authentication.signup_or_login_page_steps import SignupOrLoginPageSteps
from tools.allure.epics import AllureEpic
from tools.allure.features import AllureFeature
from tools.allure.stories import AllureStory


@pytest.mark.regression
@pytest.mark.authorization
@allure.epic(AllureEpic.USER_MANAGEMENT)
@allure.feature(AllureFeature.AUTHORIZATION)
@allure.parent_suite(AllureEpic.USER_MANAGEMENT)
@allure.suite(AllureFeature.AUTHORIZATION)
class TestAuthorization:
    @allure.story(AllureStory.SUCCESSFUL_AUTHORIZATION)
    @allure.sub_suite(AllureStory.SUCCESSFUL_AUTHORIZATION)
    @allure.title("User login with correct email and password")
    @allure.severity(allure.severity_level.CRITICAL)
    def test_successful_authorization(
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

    @allure.story(AllureStory.FAILED_AUTHORIZATION)
    @allure.sub_suite(AllureStory.FAILED_AUTHORIZATION)
    @allure.title("User login with wrong email and password")
    @allure.severity(allure.severity_level.CRITICAL)
    def test_wrong_email_and_password_authorization(self, signup_or_login_page_steps: SignupOrLoginPageSteps):
        signup_or_login_page_steps.open_page()
        signup_or_login_page_steps.login_to_account(
            email='incorrect.email@gmail.com',
            password='incorrect.password'
        )
        signup_or_login_page_steps.verify_error_login_display()
