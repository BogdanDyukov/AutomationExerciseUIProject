from playwright.sync_api import Page

from components.base_component import BaseComponent
from elements.clickable.button import Button
from elements.fields.input import Input
from elements.static.text import Text


class PaymentFormComponent(BaseComponent):
    def __init__(self, page: Page):
        super().__init__(page)

        self._card_name_input = Input(page, '//input[@data-qa="name-on-card"]', 'Card Name')
        self._card_number_input = Input(page, '//input[@data-qa="card-number"]', 'Card Number')
        self._cvc_input = Input(page, '//input[@data-qa="cvc"]', 'CVC')
        self._expiry_month_input = Input(page, '//input[@data-qa="expiry-month"]', 'Expiry Month')
        self._expiry_year_input = Input(page, '//input[@data-qa="expiry-year"]', 'Expiry Year')

        self._pay_button = Button(page, '//button[@data-qa="pay-button"]', 'Pay')

    def check_fields(
            self,
            card_name: str = '',
            card_number: str = '',
            cvc: str = '',
            expiry_month: str = '',
            expiry_year: str = ''
    ):
        self._card_name_input.check_visible()
        self._card_name_input.check_have_value(card_name)

        self._card_number_input.check_visible()
        self._card_number_input.check_have_value(card_number)

        self._cvc_input.check_visible()
        self._cvc_input.check_have_value(cvc)

        self._expiry_month_input.check_visible()
        self._expiry_month_input.check_have_value(expiry_month)

        self._expiry_year_input.check_visible()
        self._expiry_year_input.check_have_value(expiry_year)

    def check_pay_button(self):
        self._pay_button.check_visible()
        self._pay_button.check_have_text('Pay and Confirm Order')

    def check_all(
            self,
            card_name: str = '',
            card_number: str = '',
            cvc: str = '',
            expiry_month: str = '',
            expiry_year: str = ''
    ):
        self.check_fields(card_name, card_number, cvc, expiry_month, expiry_year)
        self.check_pay_button()

    def fill_fields(
            self,
            card_name: str,
            card_number: str,
            cvc: str,
            expiry_month: str,
            expiry_year: str
    ):
        self._card_name_input.fill(card_name)
        self._card_number_input.fill(card_number)
        self._cvc_input.fill(cvc)
        self._expiry_month_input.fill(expiry_month)
        self._expiry_year_input.fill(expiry_year)

    def click_pay_button(self):
        self._pay_button.click()
