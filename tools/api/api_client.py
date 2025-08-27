from http import HTTPStatus
from urllib.parse import urlencode

import requests

from models.test_user import TestUser
from config.settings import settings


def check_products_for_query_match(verified_product_ids: set[int], search_query: str):
    response = requests.post(
        url=settings.get_base_url() + '/api/searchProduct',
        headers={
            'Content-Type': 'application/x-www-form-urlencoded'
        },
        data=urlencode({"search_product": search_query})
    )

    assert response.json()['responseCode'] == HTTPStatus.OK, 'Unsuccessful product search'

    required_product_ids = set(map(lambda product: product['id'], response.json()['products']))

    assert verified_product_ids == required_product_ids, \
        f'The product does not match the search query: "{search_query}"'


def get_category(product_id: int):
    response = requests.get(url=settings.get_base_url() + '/api/productsList')

    for product in response.json()['products']:
        if product['id'] == product_id:
            return product['category']['category']

    raise ValueError(f"Product with id={product_id} not found")


def create_user_account(test_user: TestUser):
    user_data_for_create = {
        **test_user.account_information.model_dump(),
        **test_user.date_of_birth.model_dump(),
        **test_user.address_information.model_dump()
    }

    response = requests.post(
        url=settings.get_base_url() + '/api/createAccount',
        headers={
            'Content-Type': 'application/x-www-form-urlencoded'
        },
        data=urlencode(user_data_for_create)
    )

    assert response.json()['responseCode'] == HTTPStatus.CREATED, 'Account not created!'


def delete_user_account(test_user: TestUser):
    user_data_for_delete = {
        "email": test_user.account_information.email,
        "password": test_user.account_information.password
    }

    response = requests.delete(
        url=settings.get_base_url() + '/api/deleteAccount',
        headers={
            'Content-Type': 'application/x-www-form-urlencoded'
        },
        data=urlencode(user_data_for_delete)
    )

    assert response.json()['responseCode'] == HTTPStatus.OK, 'Account not deleted!'
