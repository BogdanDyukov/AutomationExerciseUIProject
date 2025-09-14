import allure
import pytest

from pages.home_page import HomePage
from tools.allure.epics import AllureEpic
from tools.allure.features import AllureFeature
from tools.allure.stories import AllureStory


@pytest.mark.regression
@pytest.mark.scroll
@allure.epic(AllureEpic.NAVIGATION)
@allure.feature(AllureFeature.SCROLL)
@allure.parent_suite(AllureEpic.NAVIGATION)
@allure.suite(AllureFeature.SCROLL)
class TestScroll:
    @allure.story(AllureStory.SCROLL_TO_TOP)
    @allure.sub_suite(AllureStory.SCROLL_TO_TOP)
    @allure.title('Check the correct operation of the scroll to the top of the page')
    @allure.severity(allure.severity_level.MINOR)
    def test_scroll_up_using_button(self, home_page: HomePage):
        home_page.open()
        home_page.navbar_component.check_logo_link()
        home_page.scroll_to_bottom()
        home_page.subscribe_to_updates_component.check_title()
        home_page.click_scroll_up_link()
        home_page.navbar_component.check_logo_link()
