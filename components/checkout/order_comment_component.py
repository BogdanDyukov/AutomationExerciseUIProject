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
        self._note_label.check_visible()
        self._note_label.check_have_text(
            'If you would like to add a comment about your order, please write it in the field below.'
        )

    def check_fields(self, message: str = ''):
        self._message_textarea.check_visible()
        self._message_textarea.check_have_value(message)

    def check_all(self, message: str = ''):
        self.check_note_label()
        self.check_fields(message=message)

    def fill_fields(self, message: str):
        self._message_textarea.fill(message)
