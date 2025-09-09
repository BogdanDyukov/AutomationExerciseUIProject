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
        self._home_link.check_visible()
        self._home_link.check_have_text(' Home')

    def check_products_link(self):
        self._products_link.check_visible()
        self._products_link.check_have_text(' Products')

    def check_cart_link(self):
        self._cart_link.check_visible()
        self._cart_link.check_have_text(' Cart')

    def check_test_cases_link(self):
        self._test_cases_link.check_visible()
        self._test_cases_link.check_have_text(' Test Cases')

    def check_api_testing_link(self):
        self._api_testing_link.check_visible()
        self._api_testing_link.check_have_text(' API Testing')

    def check_video_tutorials_link(self):
        self._video_tutorials_link.check_visible()
        self._video_tutorials_link.check_have_text(' Video Tutorials')

    def check_contact_us_link(self):
        self._contact_us_link.check_visible()
        self._contact_us_link.check_have_text(' Contact us')

    def check_signup_or_login_link(self):
        self._signup_or_login_link.check_visible()
        self._signup_or_login_link.check_have_text(' Signup / Login')

    def check_logout_link(self):
        self._logout_link.check_visible()
        self._logout_link.check_have_text(' Logout')

    def check_delete_account_link(self):
        self._delete_account_link.check_visible()
        self._delete_account_link.check_have_text(' Delete Account')

    def check_logged_in_user_text(self, username: str):
        self._logged_in_user_text.check_visible()
        self._logged_in_user_text.check_have_text(f' Logged in as {username}')

    def _check_shared_links(self):
        self.check_logo_link()
        self.check_home_link()
        self.check_products_link()
        self.check_cart_link()
        self.check_test_cases_link()
        self.check_api_testing_link()
        self.check_video_tutorials_link()
        self.check_contact_us_link()

    def check_all_as_guest(self):
        self._check_shared_links()

        self.check_signup_or_login_link()

    def check_all_as_login_user(self, username: str):
        self._check_shared_links()

        self.check_logout_link()
        self.check_delete_account_link()

        self.check_logged_in_user_text(username)

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
