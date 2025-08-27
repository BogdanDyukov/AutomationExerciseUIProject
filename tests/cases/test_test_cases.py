from pages.home_page import HomePage
from pages.cases.test_cases_page import TestCasesPage


class TestTestCases:
    def test_successful_navigation_to_test_cases_page(self, home_page: HomePage, test_cases_page: TestCasesPage):
        home_page.open()
        home_page.navbar_component.check_logo_link()
        home_page.navbar_component.click_test_cases_link()

        test_cases_page.is_open()
        test_cases_page.check_title()
