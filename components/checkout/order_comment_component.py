import allure
from playwright.sync_api import Page

from components.base_component import BaseComponent
from elements.fields.textarea import Textarea
from elements.static.label import Label


class OrderCommentComponent(BaseComponent):
    def __init__(self, page: Page):
        super().__init__(page)

        self._note_label = Label(page, '//div[@id="ordermsg"]//label', 'Note')

        self._message_textarea = Textarea(page, '//div[@id="ordermsg"]//textarea', 'Message')

    def check_note_label(self):
        expected_text = 'If you would like to add a comment about your order, please write it in the field below.'

        with allure.step(f'Check visible order comment note label with text "{expected_text}"'):
            self._note_label.check_visible()
            self._note_label.check_have_text(expected_text)

    @allure.step('Check visible order comment fields')
    def check_fields(self, message: str = ''):
        self._message_textarea.check_visible()
        self._message_textarea.check_have_value(message)

    @allure.step('Fill order comment fields')
    def fill_fields(self, message: str):
        self._message_textarea.fill(message)
