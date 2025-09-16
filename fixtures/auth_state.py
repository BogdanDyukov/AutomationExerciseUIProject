import pytest
from filelock import FileLock
from playwright.sync_api import Playwright

from config.routes import AppRoute
from config.settings import settings
from data.test_users import get_test_user
from pages.authentication.signup_or_login_page import SignupOrLoginPage
from steps.authentication.signup_or_login_page_steps import SignupOrLoginPageSteps
from tools.api.users import create_user_account, delete_user_account
from tools.playwright.mocks import abort_ads_script


@pytest.fixture(scope='session', autouse=True)
def initialize_browser_state(playwright: Playwright):
    test_user = None

    try:
        with FileLock(str(settings.browser_state_file) + ".lock"):
            if settings.browser_state_file.read_text() == '':
                browser = playwright.chromium.launch(headless=settings.headless)
                context = browser.new_context(base_url=settings.get_base_url())
                page = context.new_page()
                abort_ads_script(page)

                test_user = get_test_user()
                create_user_account(test_user)

                signup_or_login_page_steps = SignupOrLoginPageSteps(
                    signup_or_login_page=SignupOrLoginPage(page=page, path=AppRoute.SIGNUP_OR_LOGIN)
                )

                signup_or_login_page_steps.open_page()
                signup_or_login_page_steps.login_to_account(
                    email=test_user.account_information.email,
                    password=test_user.account_information.password
                )

                context.storage_state(path=settings.browser_state_file)
                browser.close()
        yield
    finally:
        if test_user:
            delete_user_account(test_user)
