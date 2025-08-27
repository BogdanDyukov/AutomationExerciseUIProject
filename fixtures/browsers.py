import pytest
from playwright.sync_api import Page, Playwright

from config.settings import settings


@pytest.fixture
def chromium_page(playwright: Playwright) -> Page:
    browser = playwright.chromium.launch(headless=settings.headless)
    context = browser.new_context(base_url=settings.get_base_url())
    yield context.new_page()
    browser.close()


@pytest.fixture
def chromium_page_with_state(playwright: Playwright) -> Page:
    browser = playwright.chromium.launch(headless=settings.headless)
    context = browser.new_context(base_url=settings.get_base_url(), storage_state=settings.browser_state_file)
    yield context.new_page()
    browser.close()


# @pytest.fixture(scope='session', autouse=True)
# def initialize_browser_state(playwright: Playwright):
#     browser = playwright.chromium.launch(headless=settings.headless)
#     context = browser.new_context(base_url=settings.get_base_url())
#     page = context.new_page()
#
#     signup_or_login_page = SignupOrLoginPage(page=page, path=AppRoute.SIGNUP_OR_LOGIN)
#     signup_page = SignupPage(page=page, path=AppRoute.SIGNUP)
#
#     signup_or_login_page.open()
#     signup_or_login_page.signup_form_component.fill_fields(
#         name=authorized_test_user.username,
#         email=authorized_test_user.email
#     )
#     signup_or_login_page.signup_form_component.click_signup_button()
#
#     signup_page.account_information_component.fill_fields(
#         gender=authorized_test_user.gender,
#         name=authorized_test_user.username,
#         password=authorized_test_user.password,
#         day_value=authorized_test_user.date_of_birth.birth_day,
#         month_value=authorized_test_user.date_of_birth.birth_month_number,
#         year_value=authorized_test_user.date_of_birth.birth_year,
#         newsletter_flag=True,
#         special_offers_flag=True
#     )
#     signup_page.address_information_component.fill_fields(
#         first_name=authorized_test_user.address_information.first_name,
#         last_name=authorized_test_user.address_information.last_name,
#         company=authorized_test_user.address_information.company,
#         first_address=authorized_test_user.address_information.address,
#         second_address=authorized_test_user.address_information.address2,
#         country_value=authorized_test_user.address_information.country,
#         state=authorized_test_user.address_information.state,
#         city=authorized_test_user.address_information.city,
#         zipcode=authorized_test_user.address_information.zipcode,
#         mobile_number=authorized_test_user.address_information.mobile_number
#     )
#     signup_page.click_create_account_button()
#
#     context.storage_state(path=settings.browser_state_file)
#
#     browser.close()
#
#     yield
#
#     browser = playwright.chromium.launch(headless=settings.headless)
#     context = browser.new_context(
#         base_url=settings.get_base_url(),
#         storage_state=settings.browser_state_file,
#     )
#
#     home_page = HomePage(page=context.new_page(), path=AppRoute.HOME)
#     home_page.open()
#     home_page.navbar_component.click_delete_account_link()
#
#     browser.close()
