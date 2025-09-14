import allure
import pytest

from config.settings import settings
from pages.contact_us.contact_us_page import ContactUsPage
from pages.home_page import HomePage
from tools.allure.epics import AllureEpic
from tools.allure.features import AllureFeature
from tools.allure.stories import AllureStory


@pytest.mark.regression
@pytest.mark.contact
@allure.epic(AllureEpic.INTERACTIONS)
@allure.feature(AllureFeature.CONTACT)
@allure.parent_suite(AllureEpic.INTERACTIONS)
@allure.suite(AllureFeature.CONTACT)
class TestContactUs:
    @allure.story(AllureStory.SUCCESSFUL_FEEDBACK)
    @allure.sub_suite(AllureStory.SUCCESSFUL_FEEDBACK)
    @allure.title('Checking the success of sending a feedback')
    @allure.severity(allure.severity_level.MINOR)
    def test_successful_feedback_submit(
            self,
            home_page_with_state: HomePage,
            contact_us_page_with_state: ContactUsPage
    ):
        # Для корректной обработки диалогового окна необходимо дожидаться загрузки скриптов (где вызывается alert)
        # Если этого не сделать, то при нажатии на кнопку alert просто не будет вызван
        # В is_open я добавил соответствующее ожидание
        contact_us_page_with_state.open()
        contact_us_page_with_state.contact_form_component.check_title()
        contact_us_page_with_state.contact_form_component.fill_fields(
            name='Bogdan',
            email='user@mail.ru',
            subject='Problem with user interface',
            message='On product card pages, some cards have a higher height '
                    'than the standard ones. Which causes strange offsets.',
            file_path=settings.test_data.image_file
        )
        contact_us_page_with_state.register_accept_dialog_handler()
        contact_us_page_with_state.contact_form_component.click_submit_button()
        contact_us_page_with_state.contact_form_component.check_success_submit_alert()
        contact_us_page_with_state.contact_form_component.click_home_button()

        home_page_with_state.is_open()
