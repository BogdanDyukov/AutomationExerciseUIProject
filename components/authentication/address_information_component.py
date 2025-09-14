import allure
from playwright.sync_api import Page

from components.base_component import BaseComponent
from elements.fields.dropdown import Dropdown
from elements.fields.input import Input
from elements.static.title import Title


class AddressInformationComponent(BaseComponent):
    def __init__(self, page: Page):
        super().__init__(page)

        self._title = Title(
            page, '//div/form/h2[@class="title text-center"]', 'Address Information'
        )

        self._first_name_input = Input(page, '//input[@data-qa="first_name"]', 'First Name')
        self._last_name_input = Input(page, '//input[@data-qa="last_name"]', 'Last Name')
        self._company_input = Input(page, '//input[@data-qa="company"]', 'Company')
        self._first_address_input = Input(page, '//input[@data-qa="address"]', 'Address')
        self._second_address_input = Input(page, '//input[@data-qa="address2"]', 'Address2')
        self._country_dropdown = Dropdown(page, '//select[@data-qa="country"]', 'Country')
        self._state_input = Input(page, '//input[@data-qa="state"]', 'State')
        self._city_input = Input(page, '//input[@data-qa="city"]', 'City')
        self._zipcode_input = Input(page, '//input[@data-qa="zipcode"]', 'Zip Code')
        self._mobile_number_input = Input(page, '//input[@data-qa="mobile_number"]', 'Mobile Number')

    def check_title(self):
        expected_title = 'Address Information'

        with allure.step(f'Check visible address information title with text "{expected_title}"'):
            self._title.check_visible()
            self._title.check_have_text(expected_title)

    @allure.step('Check visible address information fields')
    def check_fields(
            self,
            first_name: str = '',
            last_name: str = '',
            company: str = '',
            first_address: str = '',
            second_address: str = '',
            country_value: str = 'India',
            state: str = '',
            city: str = '',
            zipcode: str = '',
            mobile_number: str = ''
    ):
        self._first_name_input.check_visible()
        self._first_name_input.check_have_value(first_name)

        self._last_name_input.check_visible()
        self._last_name_input.check_have_value(last_name)

        self._company_input.check_visible()
        self._company_input.check_have_value(company)

        self._first_address_input.check_visible()
        self._first_address_input.check_have_value(first_address)

        self._second_address_input.check_visible()
        self._second_address_input.check_have_value(second_address)

        self._country_dropdown.check_visible()
        self._country_dropdown.check_have_value(country_value)

        self._state_input.check_visible()
        self._state_input.check_have_value(state)

        self._city_input.check_visible()
        self._city_input.check_have_value(city)

        self._zipcode_input.check_visible()
        self._zipcode_input.check_have_value(zipcode)

        self._mobile_number_input.check_visible()
        self._mobile_number_input.check_have_value(mobile_number)

    @allure.step('Fill address information fields')
    def fill_fields(
            self,
            first_name: str,
            last_name: str,
            first_address: str,
            country_value: str,
            state: str,
            city: str,
            zipcode: str,
            mobile_number: str,
            company: str = '',
            second_address: str = ''
    ):
        self._first_name_input.fill(first_name)
        self._last_name_input.fill(last_name)
        self._company_input.fill(company)
        self._first_address_input.fill(first_address)
        self._second_address_input.fill(second_address)

        self._country_dropdown.select_option(country_value)

        self._state_input.fill(state)
        self._city_input.fill(city)
        self._zipcode_input.fill(zipcode)
        self._mobile_number_input.fill(mobile_number)
