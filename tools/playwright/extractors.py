from playwright.sync_api import Page


def extract_product_ids(page: Page, locator_with_data_id: str) -> set[int]:
    return set(
        int(elem.get_attribute('data-product-id'))
        for elem in page.locator(locator_with_data_id).all()
    )
