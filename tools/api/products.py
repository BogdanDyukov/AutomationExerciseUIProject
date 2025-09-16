from http import HTTPStatus
from urllib.parse import urlencode

import requests

from config.settings import settings


def check_products_for_query_match(verified_product_ids: list[int], search_query: str):
    response = requests.post(
        url=settings.get_base_url() + '/api/searchProduct',
        headers={
            'Content-Type': 'application/x-www-form-urlencoded'
        },
        data=urlencode({"search_product": search_query})
    )

    assert response.json()['responseCode'] == HTTPStatus.OK, 'Unsuccessful product search'

    required_product_ids = set(map(lambda product: product['id'], response.json()['products']))

    assert set(verified_product_ids) == required_product_ids, \
        f'The product does not match the search query: "{search_query}"'


def get_products_info(products_id: list[int]) -> list[dict]:
    response = requests.get(url=settings.get_base_url() + '/api/productsList')
    return list(filter(lambda product: product['id'] in products_id, response.json()['products']))
