from http import HTTPStatus
from urllib.parse import urlencode

import requests
from pydantic import FilePath

from models.test_user import TestUser
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


def create_user_account(test_user: TestUser):
    user_data_for_create = {
        "title": test_user.account_information.gender.value,
        "name": test_user.account_information.name,
        "email": test_user.account_information.email,
        "password": test_user.account_information.password,
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


def is_user_exists(test_user: TestUser) -> bool:
    user_data_for_check = {
        "email": test_user.account_information.email,
        "password": test_user.account_information.password
    }

    response = requests.post(
        url=settings.get_base_url() + '/api/verifyLogin',
        headers={
            'Content-Type': 'application/x-www-form-urlencoded'
        },
        data=urlencode(user_data_for_check)
    )

    return response.json()['responseCode'] == HTTPStatus.OK
