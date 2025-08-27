from playwright.sync_api import Page, expect

from components.base_component import BaseComponent
from elements.static.text import Text


class ContactInfoComponent(BaseComponent):
    def __init__(self, page: Page):
        super().__init__(page)

        self._title = Text(page, '//h2[text()="Feedback For Us"]', 'Title')
        self._note_text = Text(page, '(//address/p)[1]', 'Note')
        self._instructions_text = Text(page, '(//address/p)[2]', 'Instructions')
        self._improvement_suggestion_text = Text(page, '(//address/p)[3]', 'Improvement Suggestion')
        self._thank_you_text = Text(page, '(//address/p)[4]', 'Thank You')

    def check_title(self):
        self._title.check_visible()
        self._title.check_have_text('Feedback For Us')

    def check_note_text(self):
        expect(self._note_text).to_be_visible()
        expect(self._note_text).to_have_text('We really appreciate your response to our website.')

    def check_instructions_text(self):
        expect(self._instructions_text).to_be_visible()
        expect(self._instructions_text).to_have_text(
            'Kindly share your feedback with us at feedback@automationexercise.com.'
        )

    def check_improvement_suggestion_text(self):
        expect(self._improvement_suggestion_text).to_be_visible()
        expect(self._improvement_suggestion_text).to_have_text(
            'If you have any suggestion areas or improvements, do let us know. We will definitely work on it.'
        )

    def check_thank_you_text(self):
        expect(self._thank_you_text).to_be_visible()
        expect(self._thank_you_text).to_have_text('Thank you')

    def check_all(self):
        self.check_title()
        self.check_note_text()
        self.check_instructions_text()
        self.check_improvement_suggestion_text()
        self.check_thank_you_text()
