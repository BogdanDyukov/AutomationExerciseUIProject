from playwright.sync_api import Page


def extract_product_ids_by_data_product_id(page: Page, locator_with_data_id: str) -> list[int]:
    return [
        int(elem.get_attribute('data-product-id'))
        for elem in page.locator(locator_with_data_id).all()
    ]


def extract_product_ids_by_href(page: Page, locator_with_data_id: str) -> list[int]:
    return [
        int(elem.get_attribute('href')[-1])
        for elem in page.locator(locator_with_data_id).all()
    ]

