import allure
from playwright.sync_api import Page

from components.base_component import BaseComponent
from elements.static.subtitle import Subtitle
from elements.static.text import Text
from models.test_user import Gender


class AddressDeliveryComponent(BaseComponent):
    def __init__(self, page: Page):
        super().__init__(page)

        self._title = Subtitle(page, '//ul[@id="address_delivery"]//h3', 'Delivery Address Title')
        self._gender_and_firstname_and_lastname_text = Text(
            page, '(//ul[@id="address_delivery"]//li)[2]', 'Address Firstname And Lastname'
        )
        self._company_text = Text(page, '(//ul[@id="address_delivery"]//li)[3]', 'Company')
        self._first_address_text = Text(page, '(//ul[@id="address_delivery"]//li)[4]', 'First Address')
        self._second_address_text = Text(page, '(//ul[@id="address_delivery"]//li)[5]', 'Second Address')
        self._self_city_and_state_and_postcode_text = Text(
            page, '(//ul[@id="address_delivery"]//li)[6]', 'City And State And Postcode'
        )
        self._country_text = Text(page, '(//ul[@id="address_delivery"]//li)[7]', 'Country')
        self._mobile_number_text = Text(page, '(//ul[@id="address_delivery"]//li)[8]', 'Mobile Number')

    def check_title(self):
        expected_text = 'Your delivery address'

        with allure.step(f'Check visible address delivery title with text "{expected_text}"'):
            self._title.check_visible()
            self._title.check_have_text(expected_text)

    @allure.step('Check visible address delivery gender "{gender}" '
                 'and firstname "{first_name}" and lastname "last_name" text')
    def check_gender_and_firstname_and_lastname_text(self, first_name: str, last_name: str, gender: Gender):
        self._gender_and_firstname_and_lastname_text.check_visible()
        self._gender_and_firstname_and_lastname_text.check_have_text(f'{gender}. {first_name} {last_name}')

    @allure.step('Check visible address delivery company text "{company}"')
    def check_company_text(self, company: str):
        self._company_text.check_visible()
        self._company_text.check_have_text(company)

    @allure.step('Check visible address delivery first address text "{first_address}"')
    def check_first_address_text(self, first_address: str):
        self._first_address_text.check_visible()
        self._first_address_text.check_have_text(first_address)

    @allure.step('Check visible address delivery second address text "{second_address}"')
    def check_second_address_text(self, second_address: str):
        self._second_address_text.check_visible()
        self._second_address_text.check_have_text(second_address)

    @allure.step('Check visible city "{city}" and state "{state}" and postcode "{postcode}" text')
    def check_city_and_state_and_postcode_text(self, city: str, state: str, postcode: str):
        self._self_city_and_state_and_postcode_text.check_visible()
        self._self_city_and_state_and_postcode_text.check_have_text(f'{city} {state} {postcode}')

    @allure.step('Check visible address delivery country text "{country}"')
    def check_country_text(self, country: str):
        self._country_text.check_visible()
        self._country_text.check_have_text(country)

    @allure.step('Check visible address delivery mobile number text "{mobile_number}"')
    def check_mobile_number_text(self, mobile_number: str):
        self._mobile_number_text.check_visible()
        self._mobile_number_text.check_have_text(mobile_number)

