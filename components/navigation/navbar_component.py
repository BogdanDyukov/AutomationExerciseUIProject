import allure
from playwright.sync_api import Page

from components.base_component import BaseComponent
from elements.clickable.link import Link
from elements.static.text import Text


class NavbarComponent(BaseComponent):
    def __init__(self, page: Page):
        super().__init__(page)

        self._logo_link = Link(page, '(//a[@href="/"])[1]', 'Logo')
        self._home_link = Link(page, '//a[text()=" Home"]', 'Home')
        self._products_link = Link(page, '//a[text()=" Products"]', 'Products')
        self._cart_link = Link(page, '//a[text()=" Cart"]', 'Cart')
        self._test_cases_link = Link(page, '//a[text()=" Test Cases"]', 'Test Cases')
        self._api_testing_link = Link(page, '//a[text()=" API Testing"]', 'API Testing')
        self._video_tutorials_link = Link(page, '//a[text()=" Video Tutorials"]', 'Video Tutorials')
        self._contact_us_link = Link(page, '//a[text()=" Contact us"]', 'Contact Us')
        self._signup_or_login_link = Link(page, '//a[text()=" Signup / Login"]', 'Signup / Login')
        self._logout_link = Link(page, '//a[@href="/logout"]', 'Logout')
        self._delete_account_link = Link(page, '//a[@href="/delete_account"]', 'Delete Account')

        self._logged_in_user_text = Text(page, '//a[text()=" Logged in as "]', 'Logged In User')

    def check_logo_link(self):
        self._logo_link.check_visible()

    def check_home_link(self):
        expected_text = ' Home'

        with allure.step(f'Check visible navbar home link with text "{expected_text}"'):
            self._home_link.check_visible()
            self._home_link.check_have_text(expected_text)

    def check_products_link(self):
        expected_text = ' Products'

        with allure.step(f'Check visible navbar products link with text "{expected_text}"'):
            self._products_link.check_visible()
            self._products_link.check_have_text(expected_text)

    def check_cart_link(self):
        expected_text = ' Cart'

        with allure.step(f'Check visible navbar cart link with text "{expected_text}"'):
            self._cart_link.check_visible()
            self._cart_link.check_have_text(expected_text)

    def check_test_cases_link(self):
        expected_text = ' Test Cases'

        with allure.step(f'Check visible navbar test cases link with text "{expected_text}"'):
            self._test_cases_link.check_visible()
            self._test_cases_link.check_have_text(expected_text)

    def check_api_testing_link(self):
        expected_text = ' API Testing'

        with allure.step(f'Check visible navbar API testing link with text "{expected_text}"'):
            self._api_testing_link.check_visible()
            self._api_testing_link.check_have_text(expected_text)

    def check_video_tutorials_link(self):
        expected_text = ' Video Tutorials'

        with allure.step(f'Check visible navbar video tutorials link with text "{expected_text}"'):
            self._video_tutorials_link.check_visible()
            self._video_tutorials_link.check_have_text(expected_text)

    def check_contact_us_link(self):
        expected_text = ' Contact us'

        with allure.step(f'Check visible navbar contact us link with text "{expected_text}"'):
            self._contact_us_link.check_visible()
            self._contact_us_link.check_have_text(expected_text)

    def check_signup_or_login_link(self):
        expected_text = ' Signup / Login'

        with allure.step(f'Check visible navbar signup/login link with text "{expected_text}"'):
            self._signup_or_login_link.check_visible()
            self._signup_or_login_link.check_have_text(expected_text)

    def check_logout_link(self):
        expected_text = ' Logout'

        with allure.step(f'Check visible navbar logout link with text "{expected_text}"'):
            self._logout_link.check_visible()
            self._logout_link.check_have_text(expected_text)

    def check_delete_account_link(self):
        expected_text = ' Delete Account'

        with allure.step(f'Check visible navbar delete account link with text "{expected_text}"'):
            self._delete_account_link.check_visible()
            self._delete_account_link.check_have_text(expected_text)

    def check_logged_in_user_text(self, username: str):
        expected_text = f' Logged in as {username}'

        with allure.step(f'Check visible navbar logged in user text with text "{expected_text}"'):
            self._logged_in_user_text.check_visible()
            self._logged_in_user_text.check_have_text(expected_text)

    def click_home_link(self):
        self._home_link.click()

    def click_products_link(self):
        self._products_link.click()

    def click_cart_link(self):
        self._cart_link.click()

    def click_test_cases_link(self):
        self._test_cases_link.click()

    def click_api_testing_link(self):
        self._api_testing_link.click()

    def click_video_tutorials_link(self):
        self._video_tutorials_link.click()

    def click_contact_us_link(self):
        self._contact_us_link.click()

    def click_signup_or_login_link(self):
        self._signup_or_login_link.click()

    def click_logout_link(self):
        self._logout_link.click()

    def click_delete_account_link(self):
        self._delete_account_link.click()
