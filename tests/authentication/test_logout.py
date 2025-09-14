import allure
import pytest

from models.test_user import TestUser
from steps.authentication.signup_or_login_page_steps import SignupOrLoginPageSteps
from steps.home_page_steps import HomePageSteps
from tools.allure.epics import AllureEpic
from tools.allure.features import AllureFeature
from tools.allure.stories import AllureStory


@pytest.mark.regression
@pytest.mark.logout
@allure.epic(AllureEpic.USER_MANAGEMENT)
@allure.feature(AllureFeature.LOGOUT)
@allure.parent_suite(AllureEpic.USER_MANAGEMENT)
@allure.suite(AllureFeature.LOGOUT)
class TestLogout:
    @allure.story(AllureStory.SUCCESSFUL_LOGOUT)
    @allure.sub_suite(AllureStory.SUCCESSFUL_LOGOUT)
    @allure.title("Correct logout of account")
    @allure.severity(allure.severity_level.NORMAL)
    def test_successful_logout(
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
