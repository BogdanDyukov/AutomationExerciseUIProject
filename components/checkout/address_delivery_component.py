from playwright.sync_api import Page

from components.base_component import BaseComponent
from elements.static.subtitle import Subtitle
from elements.static.text import Text
from models.test_user import Gender


class AddressDeliveryComponent(BaseComponent):
    def __init__(self, page: Page):
        super().__init__(page)

        self._title = Subtitle(page, '//ul[@id="address_delivery"]//h3', 'Delivery Address Title')
        self._firstname_and_lastname_text = Text(
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
        self._title.check_visible()
        self._title.check_have_text('Your delivery address')

    def check_firstname_and_lastname_text(self, first_name: str, last_name: str, gender: Gender):
        self._firstname_and_lastname_text.check_visible()
        self._firstname_and_lastname_text.check_have_text(f'{gender}. {first_name} {last_name}')

    def check_company_text(self, company: str):
        self._company_text.check_visible()
        self._company_text.check_have_text(company)

    def check_first_address_text(self, first_address: str):
        self._first_address_text.check_visible()
        self._first_address_text.check_have_text(first_address)

    def check_second_address_text(self, second_address: str):
        self._second_address_text.check_visible()
        self._second_address_text.check_have_text(second_address)

    def check_city_and_state_and_postcode_text(self, city: str, state: str, postcode: str):
        self._self_city_and_state_and_postcode_text.check_visible()
        self._self_city_and_state_and_postcode_text.check_have_text(f'{city} {state} {postcode}')

    def check_country_text(self, country: str):
        self._country_text.check_visible()
        self._country_text.check_have_text(country)

    def check_mobile_number_text(self, mobile_number: str):
        self._mobile_number_text.check_visible()
        self._mobile_number_text.check_have_text(mobile_number)

    def check_all(
            self,
            first_name: str,
            last_name: str,
            gender: Gender,
            company: str,
            first_address: str,
            second_address: str,
            city: str,
            state: str,
            postcode: str,
            country: str,
            mobile_number: str,
    ):
        self.check_title()
        self.check_firstname_and_lastname_text(first_name, last_name, gender)
        self.check_company_text(company)
        self.check_first_address_text(first_address)
        self.check_second_address_text(second_address)
        self.check_city_and_state_and_postcode_text(city, state, postcode)
        self.check_country_text(country)
        self.check_mobile_number_text(mobile_number)
