import allure
from playwright.sync_api import Playwright
from pydantic import FilePath

from config.settings import Browser, settings
from tools.allure.attach import attach_data
from tools.playwright.mocks import abort_ads_script


def initialize_playwright_page(
        playwright: Playwright,
        test_name: str,
        browser_type: Browser,
        storage_state: FilePath | None = None
):
    browser = playwright[browser_type].launch(headless=settings.headless)
    context = browser.new_context(
        base_url=settings.get_base_url(),
        storage_state=storage_state,
        record_video_dir=settings.videos_dir
    )
    context.tracing.start(screenshots=True, snapshots=True, sources=True)

    page = context.new_page()
    abort_ads_script(page)

    yield page

    context.tracing.stop(path=settings.tracing_dir.joinpath(f'{test_name}.zip'))
    browser.close()

    attach_data(settings.tracing_dir.joinpath(f'{test_name}.zip'), name='trace', extension='zip')
    attach_data(page.video.path(), name='video', attachment_type=allure.attachment_type.WEBM)
