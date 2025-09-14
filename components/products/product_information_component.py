import allure
from playwright.sync_api import Page

from components.base_component import BaseComponent
from elements.clickable.button import Button
from elements.media.image import Image
from elements.fields.input import Input
from elements.static.text import Text
from elements.static.title import Title


class ProductInformationComponent(BaseComponent):
    def __init__(self, page: Page):
        super().__init__(page)

        self._name_title = Title(page, '//div[@class="product-information"]/h2', 'Name')
        self._category_text = Text(
            page, '(//div[@class="product-information"]//p)[1]', 'Category'
        )
        self._rating_image = Image(page, '(//div[@class="product-information"]//img)[2]', 'Rating')
        self._price_text = Text(page, '//div[@class="product-information"]//span[contains(text(), "Rs")]', 'Price')
        self._availability_text = Text(
            page, '(//div[@class="product-information"]//p)[2]', 'Availability'
        )
        self._condition_text = Text(
            page, '(//div[@class="product-information"]//p)[3]', 'Condition'
        )
        self._brand_text = Text(page, '(//div[@class="product-information"]//p)[4]', 'Brand')

        self._quantity_input = Input(
            page, '//div[@class="product-information"]//input[@type="number"]', 'Quantity'
        )
        self._add_to_cart_button = Button(page, '//div[@class="product-information"]//button', 'Add To Cart')

    @allure.step('Check visible product information name title')
    def check_name_title(self, name: str | None = None):
        self._name_title.check_visible()

        if name:
            self._name_title.check_have_text(name)

    @allure.step('Check visible product information category text')
    def check_category_text(self, category: str | None = None):
        self._category_text.check_visible()

        if category:
            self._category_text.check_have_text('Category: ' + category)

    def check_rating_image(self):
        self._rating_image.check_visible()

    @allure.step('Check visible product information price text')
    def check_price_text(self, price: int | None = None):
        self._price_text.check_visible()

        if price:
            self._price_text.check_have_text('Rs. ' + str(price))

    @allure.step('Check visible product information availability text')
    def check_availability_text(self, availability: str | None = None):
        self._availability_text.check_visible()

        if availability:
            self._availability_text.check_have_text('Availability: ' + availability)

    @allure.step('Check visible product information condition text')
    def check_condition_text(self, condition: str | None = None):
        self._condition_text.check_visible()

        if condition:
            self._condition_text.check_have_text('Condition: ' + condition)

    @allure.step('Check visible product information brand text')
    def check_brand_text(self, brand: str | None = None):
        self._brand_text.check_visible()

        if brand:
            self._brand_text.check_have_text('Brand: ' + brand)

    @allure.step('Check visible product information fields')
    def check_fields(self, quantity: int = 1):
        self._quantity_input.check_visible()
        self._quantity_input.check_have_value(str(quantity))

    def check_add_to_cart_button(self):
        expected_text = ' Add to cart '

        with allure.step(f'Check visible product information add to cart button with text "{expected_text}"'):
            self._add_to_cart_button.check_visible()
            self._add_to_cart_button.check_have_text(expected_text)

    @allure.step('Fill product information fields')
    def fill_fields(self, quantity: int):
        self._quantity_input.fill(str(quantity))

    def click_add_to_cart_button(self):
        self._add_to_cart_button.click()
