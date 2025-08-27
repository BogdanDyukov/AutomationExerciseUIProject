from playwright.sync_api import Page

from components.authentication.account_information_component import AccountInformationComponent
from components.authentication.address_information_component import AddressInformationComponent
from components.navigation.navbar_component import NavbarComponent
from components.interactions.subscribe_to_updates_component import SubscribeToUpdatesComponent
from elements.clickable.button import Button
from pages.base.base_page import BasePage
from config.routes import AppRoute


class SignupPage(BasePage):
    def __init__(self, page: Page, path: AppRoute):
        super().__init__(page, path)

        self.navbar_component: NavbarComponent = NavbarComponent(page)
        self.account_information_component: AccountInformationComponent = AccountInformationComponent(page)
        self.address_information_component: AddressInformationComponent = AddressInformationComponent(page)
        self.subscribe_to_updates_component: SubscribeToUpdatesComponent = SubscribeToUpdatesComponent(page)

        self._create_account_button = Button(page, '//button[@data-qa="create-account"]', 'Create Account')

    def check_create_account_button(self):
        self._create_account_button.check_visible()
        self._create_account_button.check_have_text('Create Account')

    def click_create_account_button(self):
        self._create_account_button.check_visible()
        self._create_account_button.click()
