from playwright.sync_api import Page

from components.base_component import BaseComponent
from models.test_user import Gender
from elements.fields.checkbox import Checkbox
from elements.fields.dropdown import Dropdown
from elements.fields.input import Input
from elements.fields.radio_button import RadioButton
from elements.static.title import Title


class AccountInformationComponent(BaseComponent):
    def __init__(self, page: Page):
        super().__init__(page)

        self._title = Title(
            page, '//div/h2[@class="title text-center"]', 'Title'
        )

        self._male_gender_radio = RadioButton(page, '//input[@id="id_gender1"]', 'Male Gender')
        self._female_gender_radio = RadioButton(page, '//input[@id="id_gender2"]', 'Female Gender')
        self._name_input = Input(page, '//input[@data-qa="name"]', 'Name')
        self._email_input = Input(page, '//input[@data-qa="email"]', 'Email')
        self._password_input = Input(page, '//input[@data-qa="password"]', 'Password')
        self._birth_day_dropdown = Dropdown(page, '//select[@data-qa="days"]', 'Birth Day')
        self._birth_month_dropdown = Dropdown(page, '//select[@data-qa="months"]', 'Birth Month')
        self._birth_year_dropdown = Dropdown(page, '//select[@data-qa="years"]', 'Birth Year')
        self._newsletter_checkbox = Checkbox(page, '//input[@id="newsletter"]', 'Newsletter')
        self._special_offers_checkbox = Checkbox(page, '//input[@id="optin"]', 'Special Offers')

    def check_title(self):
        self._title.check_visible()
        self._title.check_have_text('Enter Account Information')

    def check_fields(
            self,
            name: str,
            email: str,
            gender: Title | None = None,
            password: str = '',
            day_value: str = '',
            month_value: str = '',
            year_value: str = '',
            newsletter_flag: bool = False,
            special_offers_flag: bool = False
    ):
        self._male_gender_radio.check_visible()
        self._female_gender_radio.check_visible()

        if gender == Gender.MR:
            self._male_gender_radio.check_checked(True)
            self._female_gender_radio.check_checked(False)
        elif gender == Gender.MRS:
            self._male_gender_radio.check_checked(False)
            self._female_gender_radio.check_checked(True)
        else:
            self._male_gender_radio.check_checked(False)
            self._female_gender_radio.check_checked(False)

        self._name_input.check_visible()
        self._name_input.check_have_value(name)

        self._email_input.check_visible()
        self._email_input.check_have_value(email)

        self._password_input.check_visible()
        self._password_input.check_have_value(password)

        self._birth_day_dropdown.check_visible()
        self._birth_day_dropdown.check_have_value(day_value)

        self._birth_month_dropdown.check_visible()
        self._birth_month_dropdown.check_have_value(month_value)

        self._birth_year_dropdown.check_visible()
        self._birth_year_dropdown.check_have_value(year_value)

        self._newsletter_checkbox.check_visible()
        self._newsletter_checkbox.check_checked(newsletter_flag)

        self._special_offers_checkbox.check_visible()
        self._special_offers_checkbox.check_checked(special_offers_flag)

    def check_all(
        self,
        name: str,
        email: str,
        gender: Gender | None = None,
        password: str = '',
        day_value: str = '',
        month_value: str = '',
        year_value: str = '',
        newsletter_flag: bool = False,
        special_offers_flag: bool = False
    ):
        self.check_title()
        self.check_fields(
            name=name,
            email=email,
            gender=gender,
            password=password,
            day_value=day_value,
            month_value=month_value,
            year_value=year_value,
            newsletter_flag=newsletter_flag,
            special_offers_flag=special_offers_flag
        )

    def fill_fields(
            self,
            name: str,
            password: str,
            gender: Gender | None = None,
            day_value: str = '',
            month_value: str = '',
            year_value: str = '',
            newsletter_flag: bool = False,
            special_offers_flag: bool = False
    ):

        if gender == Gender.MR:
            self._male_gender_radio.set_checked(True)
        elif gender == Gender.MRS:
            self._female_gender_radio.set_checked(True)

        self._name_input.fill(name)
        self._password_input.fill(password)

        self._birth_day_dropdown.select_option(day_value)
        self._birth_month_dropdown.select_option(month_value)
        self._birth_year_dropdown.select_option(year_value)

        self._newsletter_checkbox.set_checked(newsletter_flag)
        self._special_offers_checkbox.set_checked(special_offers_flag)

    def check_disabled_email_input(self):
        self._email_input.check_disabled()
