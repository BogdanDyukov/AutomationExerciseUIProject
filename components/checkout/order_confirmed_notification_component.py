from playwright.sync_api import Page
from pydantic import DirectoryPath

from components.base_notification_component import BaseNotificationComponent
from elements.clickable.button import Button
from models.notification import Notification


class OrderConfirmedNotificationComponent(BaseNotificationComponent):
    def __init__(self, page: Page, identifier: str, data: Notification):
        super().__init__(page, identifier, data)

        self._download_invoice_button = Button(page, '//a[text()="Download Invoice"]', 'Download Invoice')

    def check_download_invoice_button(self):
        self._download_invoice_button.check_visible()
        self._download_invoice_button.check_have_text('Download Invoice')

    def check_all(self):
        self._check_all()
        self.check_download_invoice_button()

    # def click_download_invoice_button(self):
    #     self._download_invoice_button.click()

    def download_invoice(self, file_path: DirectoryPath):
        with self._page.expect_download() as download_info:
            self._download_invoice_button.click()

        download = download_info.value

        full_path = str(file_path) + "/" + download.suggested_filename
        download.save_as(full_path)
