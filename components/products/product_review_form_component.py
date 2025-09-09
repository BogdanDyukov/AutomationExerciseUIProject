from playwright.sync_api import Page

from components.base_component import BaseComponent
from elements.clickable.button import Button
from elements.fields.input import Input
from elements.fields.textarea import Textarea
from elements.static.text import Text


class ProductReviewFormComponent(BaseComponent):
    def __init__(self, page: Page):
        super().__init__(page)

        self._write_your_review_text = Text(page, '//a[@data-toggle="tab"]', 'Title')

        self._name_input = Input(page, '//input[@id="name"]', 'Name')
        self._email_input = Input(page, '//input[@id="email"]', 'email')
        self._review_textarea = Textarea(page, '//textarea[@id="review"]', 'Review')

        self._submit_button = Button(page, '//button[@id="button-review"]', 'Submit')

        self._thank_you_alert = Text(page, '//span[contains(text(), "Thank you")]', 'Thank You Alert')

    def check_write_your_review_text(self):
        self._write_your_review_text.check_visible()
        self._write_your_review_text.check_have_text('Write Your Review')

    def check_name_input(self, name: str = ''):
        self._name_input.check_visible()
        self._name_input.check_have_value(name)

    def check_email_input(self, email: str = ''):
        self._email_input.check_visible()
        self._email_input.check_have_value(email)

    def check_review_textarea(self, review: str = ''):
        self._review_textarea.check_visible()
        self._review_textarea.check_have_value(review)

    def check_submit_button(self):
        self._submit_button.check_visible()
        self._submit_button.check_have_text(' Submit ')

    def check_thank_you_alert(self):
        self._thank_you_alert.check_visible()
        self._thank_you_alert.check_have_text('Thank you for your review.')

    def check_all(self, name: str = '', email: str = '', review: str = ''):
        self.check_write_your_review_text()
        self.check_name_input(name)
        self.check_email_input(email)
        self.check_review_textarea(review)
        self.check_submit_button()

    def fill_fields(self, name: str, email: str, review: str):
        self._name_input.fill(name)
        self._email_input.fill(email)
        self._review_textarea.fill(review)

    def click_submit(self):
        self._submit_button.click()
