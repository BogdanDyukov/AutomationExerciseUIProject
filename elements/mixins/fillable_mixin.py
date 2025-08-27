from elements.base_element import BaseElement


class FillableMixin:
    def fill(self: BaseElement, value: str, nth: int = 0, **kwargs):
        locator = self.get_locator(nth, **kwargs)
        locator.fill(value)
