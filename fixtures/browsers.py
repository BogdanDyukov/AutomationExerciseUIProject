import pytest
from _pytest.fixtures import SubRequest
from playwright.sync_api import Page, Playwright

from config.settings import settings
from tools.playwright.pages import initialize_playwright_page


@pytest.fixture(params=settings.browsers)
def page(request: SubRequest, playwright: Playwright) -> Page:
    yield from initialize_playwright_page(playwright, test_name=request.node.name, browser_type=request.param)


@pytest.fixture(params=settings.browsers)
def page_with_state(request: SubRequest, playwright: Playwright) -> Page:
    yield from initialize_playwright_page(
        playwright,
        test_name=request.node.name,
        browser_type=request.param,
        storage_state=settings.browser_state_file
    )
