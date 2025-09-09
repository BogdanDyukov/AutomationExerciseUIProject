from pages.home_page import HomePage


class TestScroll:
    def test_scroll_up_using_button(self, home_page: HomePage):
        home_page.open()
        home_page.navbar_component.check_logo_link()
        home_page.scroll_to_bottom()
        home_page.subscribe_to_updates_component.check_title()
        home_page.click_scroll_up_link()
        home_page.navbar_component.check_logo_link()
