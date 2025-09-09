from config.settings import PaymentCardInfo
from pages.checkout.payment_page import PaymentPage


class PaymentPageSteps:
    def __init__(self, payment_page: PaymentPage):
        self._payment_page = payment_page

    def open_page(self):
        self._payment_page.open()
        self._payment_page.check_title()

    def is_open_page(self):
        self._payment_page.is_open()
        self._payment_page.check_title()

    def enter_payment_information_and_confirm_order(self, payment_card_info: PaymentCardInfo):
        self._payment_page.payment_form_component.fill_fields(
            card_name=payment_card_info.name,
            card_number=payment_card_info.number,
            cvc=str(payment_card_info.cvc),
            expiry_month=payment_card_info.expiry_month,
            expiry_year=str(payment_card_info.expiry_year)
        )
        self._payment_page.payment_form_component.click_pay_button()
