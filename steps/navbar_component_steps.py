from components.navigation.navbar_component import NavbarComponent


class NavbarComponentSteps:

    def __init__(self, navbar_component: NavbarComponent):
        self._navbar_component = navbar_component

    def go_home(self):
        self._navbar_component.click_home_link()

    def go_products(self):
        self._navbar_component.click_products_link()

    def go_cart(self):
        self._navbar_component.click_cart_link()

    def go_test_cases(self):
        self._navbar_component.click_test_cases_link()

    def go_api_testing(self):
        self._navbar_component.click_api_testing_link()

    def go_video_tutorials(self):
        self._navbar_component.click_video_tutorials_link()

    def go_contact_us(self):
        self._navbar_component.click_contact_us_link()

    def go_signup_or_login(self):
        self._navbar_component.click_signup_or_login_link()

    def go_logout(self):
        self._navbar_component.click_logout_link()

    def go_delete_account(self):
        self._navbar_component.click_delete_account_link()

    def verify_user_logged_in(self, username: str):
        self._navbar_component.check_logged_in_user_text(username)
