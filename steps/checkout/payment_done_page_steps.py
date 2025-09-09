from pydantic import DirectoryPath

from pages.checkout.payment_done_page import PaymentDonePage


class PaymentDonePageSteps:
    def __init__(self, payment_done_page: PaymentDonePage):
        self._payment_done_page = payment_done_page

    def open_page(self, total_amount: int):
        self._payment_done_page.open(total_amount=total_amount)
        self._payment_done_page.order_notification_component.check_title()

    def is_open_page(self, total_amount: int):
        self._payment_done_page.is_open(total_amount=total_amount)
        self._payment_done_page.order_notification_component.check_title()

    def confirm_notification(self):
        self._payment_done_page.order_notification_component.click_continue_button()

    def download_invoice(self, file_path: DirectoryPath):
        self._payment_done_page.order_notification_component.download_invoice(file_path)

