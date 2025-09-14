import allure
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
        expected_text = 'Write Your Review'

        with allure.step(f'Check visible product review form review text "{expected_text}"'):
            self._write_your_review_text.check_visible()
            self._write_your_review_text.check_have_text(expected_text)

    @allure.step('Check visible product review form fields')
    def check_fields(self, name: str = '', email: str = '', review: str = ''):
        self._name_input.check_visible()
        self._name_input.check_have_value(name)

        self._email_input.check_visible()
        self._email_input.check_have_value(email)

        self._review_textarea.check_visible()
        self._review_textarea.check_have_value(review)

    def check_submit_button(self):
        expected_text = ' Submit '

        with allure.step(f'Check visible product review form submit button with text "{expected_text}"'):
            self._submit_button.check_visible()
            self._submit_button.check_have_text(expected_text)

    def check_thank_you_alert(self):
        expected_text = 'Thank you for your review.'

        with allure.step(f'Check visible product review form thank you alert with text "{expected_text}"'):
            self._thank_you_alert.check_visible()
            self._thank_you_alert.check_have_text(expected_text)

    @allure.step('Fill product review form fields')
    def fill_fields(self, name: str, email: str, review: str):
        self._name_input.fill(name)
        self._email_input.fill(email)
        self._review_textarea.fill(review)

    def click_submit(self):
        self._submit_button.click()
