from playwright.sync_api import Page

from components.base_component import BaseComponent
from elements.clickable.button import Button
from elements.clickable.link import Link
from elements.static.text import Text


class AddedToCartModalComponent(BaseComponent):
    def __init__(self, page: Page):
        super().__init__(page)

        self._title = Text(page, '//div[@id="cartModal"]//h4', 'Title')
        self._note_text = Text(page, '(//div[@id="cartModal"]//p)[1]', 'Note')

        self._view_cart_link = Link(page, '//div[@id="cartModal"]//a', 'View Cart')
        self._continue_shopping_button = Button(page, '//div[@id="cartModal"]//button', 'Continue Shopping')

    def check_title(self):
        self._title.check_visible()
        self._title.check_have_text('Added!')

    def check_note_text(self):
        self._note_text.check_visible()
        self._note_text.check_have_text('Your product has been added to cart.')

    def check_view_cart_link(self):
        self._view_cart_link.check_visible()
        self._view_cart_link.check_have_text('View Cart')

    def check_continue_shopping_button(self):
        self._continue_shopping_button.check_visible()
        self._continue_shopping_button.check_have_text('Continue Shopping')

    def check_all(self):
        self.check_title()
        self.check_note_text()
        self.check_view_cart_link()
        self.check_continue_shopping_button()

    def click_view_cart_link(self):
        self._view_cart_link.check_visible()
        self._view_cart_link.click()

    def click_continue_shopping_button(self):
        self._continue_shopping_button.check_visible()
        self._continue_shopping_button.click()
