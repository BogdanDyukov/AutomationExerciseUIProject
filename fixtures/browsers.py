import pytest
from _pytest.fixtures import SubRequest
from playwright.sync_api import Page, Playwright

from config.settings import settings


@pytest.fixture
def chromium_page(request: SubRequest, playwright: Playwright) -> Page:
    browser = playwright.chromium.launch(headless=settings.headless)
    context = browser.new_context(base_url=settings.get_base_url())
    context.tracing.start(screenshots=True, snapshots=True, sources=True)

    yield context.new_page()

    context.tracing.stop(path=settings.tracing_dir.joinpath(f'{request.node.name}.zip'))
    browser.close()


@pytest.fixture
def chromium_page_with_state(request: SubRequest, playwright: Playwright) -> Page:
    browser = playwright.chromium.launch(headless=settings.headless)
    context = browser.new_context(base_url=settings.get_base_url(), storage_state=settings.browser_state_file)
    context.tracing.start(screenshots=True, snapshots=True, sources=True)

    yield context.new_page()

    context.tracing.stop(path=settings.tracing_dir.joinpath(f'{request.node.name}.zip'))
    browser.close()


# @pytest.fixture(scope='session', autouse=True)
# def initialize_browser_state(playwright: Playwright, session_user):
#     browser = playwright.chromium.launch(headless=settings.headless)
#     context = browser.new_context(base_url=settings.get_base_url())
#     page = context.new_page()
#
#     signup_or_login_page = SignupOrLoginPage(page=page, path=AppRoute.SIGNUP_OR_LOGIN)
#
#     signup_or_login_page.open()
#     signup_or_login_page.login_form_component.fill_fields(
#         email=authorized_test_user_1.account_information.email,
#         password=authorized_test_user_1.account_information.password
#     )
#     signup_or_login_page.login_form_component.click_login_button()
#
#     context.storage_state(path=settings.browser_state_file)
#
#     browser.close()
