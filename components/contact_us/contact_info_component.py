import allure
from playwright.sync_api import Page, expect

from components.base_component import BaseComponent
from elements.static.text import Text
from elements.static.title import Title


class ContactInfoComponent(BaseComponent):
    def __init__(self, page: Page):
        super().__init__(page)

        self._title = Title(page, '//h2[text()="Feedback For Us"]', 'Feedback For Us')
        self._note_text = Text(page, '(//address/p)[1]', 'Note')
        self._instructions_text = Text(page, '(//address/p)[2]', 'Instructions')
        self._improvement_suggestion_text = Text(page, '(//address/p)[3]', 'Improvement Suggestion')
        self._thank_you_text = Text(page, '(//address/p)[4]', 'Thank You')

    def check_title(self):
        expected_text = 'Feedback For Us'

        with allure.step(f'Check visible contact info title with text "{expected_text}"'):
            self._title.check_visible()
            self._title.check_have_text(expected_text)

    def check_note_text(self):
        expected_text = 'We really appreciate your response to our website.'

        with allure.step(f'Check visible contact info note text "{expected_text}"'):
            expect(self._note_text).to_be_visible()
            expect(self._note_text).to_have_text(expected_text)

    def check_instructions_text(self):
        expected_text = 'Kindly share your feedback with us at feedback@automationexercise.com.'

        with allure.step(f'Check visible contact info instructions text "{expected_text}"'):
            expect(self._instructions_text).to_be_visible()
            expect(self._instructions_text).to_have_text(expected_text)

    def check_improvement_suggestion_text(self):
        expected_text = 'If you have any suggestion areas or improvements, do let us know. We will definitely work on it.'

        with allure.step(f'Check visible contact info improvement suggestion text "{expected_text}"'):
            expect(self._improvement_suggestion_text).to_be_visible()
            expect(self._improvement_suggestion_text).to_have_text(expected_text)

    def check_thank_you_text(self):
        expected_text = 'Thank you'

        with allure.step(f'Check visible contact info thank you text "{expected_text}"'):
            expect(self._thank_you_text).to_be_visible()
            expect(self._thank_you_text).to_have_text(expected_text)
