import allure
from playwright.sync_api import Page

from components.contact_us.contact_form_component import ContactFormComponent
from components.contact_us.contact_info_component import ContactInfoComponent
from components.navigation.navbar_component import NavbarComponent
from components.subscription.subscribe_to_updates_component import SubscribeToUpdatesComponent
from elements.static.title import Title
from pages.base.base_page import BasePage
from config.routes import AppRoute


class ContactUsPage(BasePage):
    def __init__(self, page: Page, path: AppRoute):
        super().__init__(page, path)

        self.navbar_component: NavbarComponent = NavbarComponent(page)
        self.contact_form_component: ContactFormComponent = ContactFormComponent(page)
        self.contact_info_component: ContactInfoComponent = ContactInfoComponent(page)
        self.subscribe_to_updates_component: SubscribeToUpdatesComponent = SubscribeToUpdatesComponent(page)

        self._title = Title(page, '//h2[text()="Contact "]', 'Contact Us')

    def check_title(self):
        expected_text = 'Contact Us'

        with allure.step(f'Check visible title with text "{expected_text}"'):
            self._title.check_visible()
            self._title.check_have_text(expected_text)
