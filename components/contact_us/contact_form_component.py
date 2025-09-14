import allure
from playwright.sync_api import Page

from components.base_component import BaseComponent
from elements.clickable.button import Button
from elements.fields.file_input import FileInput
from elements.fields.input import Input
from elements.static.text import Text
from elements.fields.textarea import Textarea
from elements.static.title import Title


class ContactFormComponent(BaseComponent):
    def __init__(self, page: Page):
        super().__init__(page)

        self._notification_text = Text(
            page, '//div[text()="Below contact form is for testing purpose."]', 'Notification'
        )
        self._title = Title(page, '//h2[text()="Get In Touch"]', 'Get In Touch')

        self._name_input = Input(page, '//input[@data-qa="name"]', 'Name')
        self._email_input = Input(page, '//input[@data-qa="email"]', 'Email')
        self._subject_input = Input(page, '//input[@data-qa="subject"]', 'Subject')
        self._message_textarea = Textarea(page, '//textarea[@data-qa="message"]', 'Message')
        self._upload_input = FileInput(page, '//input[@name="upload_file"]', 'Upload')

        self._submit_button = Button(page, '//input[@data-qa="submit-button"]', 'Submit')
        self._home_button = Button(page, '//div[@class="contact-form"]//a[@href="/"]', 'Home')

        self._success_submit_alert = Text(page, '(//div[contains(text(), "Success!")])[1]', 'Success Alert')

    def check_notification_text(self):
        expected_text = 'Note: Below contact form is for testing purpose.'

        with allure.step(f'Check visible contact form notification text "{expected_text}"'):
            self._notification_text.check_visible()
            self._notification_text.check_have_text(expected_text)

    def check_title(self):
        expected_text = 'Get In Touch'

        with allure.step(f'Check visible contact form title with text "{expected_text}"'):
            self._title.check_visible()
            self._title.check_have_text(expected_text)

    @allure.step('Check visible contact form fields')
    def check_fields(
            self,
            name: str = '',
            email: str = '',
            subject: str = '',
            message: str = '',
            file_path: str | None = None
    ):
        self._name_input.check_visible()
        self._name_input.check_have_value(name)

        self._email_input.check_visible()
        self._email_input.check_have_value(email)

        self._subject_input.check_visible()
        self._subject_input.check_have_value(subject)

        self._message_textarea.check_visible()
        self._message_textarea.check_have_value(message)

        self._upload_input.check_visible()

        if file_path:
            self._upload_input.check_have_value(file_path)

    def check_submit_button(self):
        expected_text = 'Submit'

        with allure.step(f'Check visible contact form submit button with text "{expected_text}"'):
            self._submit_button.check_visible()
            self._submit_button.check_have_text(expected_text)

    def check_home_button(self):
        expected_text = ' Home'

        with allure.step(f'Check visible contact form home button with text "{expected_text}"'):
            self._home_button.check_visible()
            self._home_button.check_have_text(expected_text)

    def check_success_submit_alert(self):
        expected_text = 'Success! Your details have been submitted successfully.'

        with allure.step(f'Check visible contact form success submit alert with text "{expected_text}"'):
            self._success_submit_alert.check_visible()
            self._success_submit_alert.check_have_text(expected_text)

    @allure.step('Fill contact form fields')
    def fill_fields(
            self,
            email: str,
            name: str = '',
            subject: str = '',
            message: str = '',
            file_path: str | None = None
    ):
        self._email_input.fill(email)
        self._name_input.fill(name)
        self._subject_input.fill(subject)
        self._message_textarea.fill(message)

        if file_path:
            self._upload_input.set_input_files(file_path)

    def click_submit_button(self):
        self._submit_button.click()

    def click_home_button(self):
        self._home_button.click()
