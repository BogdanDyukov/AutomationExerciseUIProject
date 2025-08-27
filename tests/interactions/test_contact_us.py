from config.settings import settings
from pages.interactions.contact_us_page import ContactUsPage
from pages.home_page import HomePage


class TestContactUs:
    def test_successful_feedback_submit(self, home_page: HomePage, contact_us_page: ContactUsPage):
        home_page.open()
        home_page.navbar_component.check_logo_link()
        home_page.navbar_component.click_contact_us_link()

        # Для корректной обработки диалогового окна необходимо дожидаться загрузки скриптов (где вызывается alert)
        # Если этого не сделать, то при нажатии на кнопку alert просто не будет вызван
        # В is_open я добавил соответствующее ожидание
        contact_us_page.is_open()
        contact_us_page.contact_form_component.check_title()
        contact_us_page.contact_form_component.fill_fields(
            name='User',
            email='user@gmail.com',
            subject='Problem with user interface',
            message='On product card pages, some cards have a higher height '
                    'than the standard ones. Which causes strange offsets.',
            file_path=settings.test_data.image_file
        )
        contact_us_page.register_accept_dialog_handler()
        contact_us_page.contact_form_component.click_submit_button()
        contact_us_page.contact_form_component.check_success_submit_alert()
        contact_us_page.contact_form_component.click_home_button()

        home_page.is_open()
