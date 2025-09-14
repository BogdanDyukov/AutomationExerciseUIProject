import json
from http import HTTPStatus
from urllib.parse import urlencode

import requests
from allure_commons.types import AttachmentType

from config.settings import settings
from tools.allure.attach import attach_data


def check_products_for_query_match(verified_product_ids: list[int], search_query: str):
    response = requests.post(
        url=settings.get_base_url() + '/api/searchProduct',
        headers={
            'Content-Type': 'application/x-www-form-urlencoded'
        },
        data=urlencode({"search_product": search_query})
    )

    attach_data(
        data=json.dumps(response.json(), indent=4, ensure_ascii=False),
        name='Products matching the query',
        attachment_type=AttachmentType.JSON
    )

    assert response.json()['responseCode'] == HTTPStatus.OK, 'Unsuccessful product search'

    required_product_ids = set(map(lambda product: product['id'], response.json()['products']))

    assert set(verified_product_ids) == required_product_ids, \
        f'The product does not match the search query: "{search_query}"'


def get_products_info(products_id: list[int]) -> list[dict]:
    response = requests.get(url=settings.get_base_url() + '/api/productsList')

    products_info = list(filter(lambda product: product['id'] in products_id, response.json()['products']))

    attach_data(
        data=json.dumps(products_info, indent=4, ensure_ascii=False),
        name='Products Info Response',
        attachment_type=AttachmentType.JSON
    )

    return products_info
