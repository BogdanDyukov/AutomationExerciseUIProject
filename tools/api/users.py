import json
from http import HTTPStatus
from urllib.parse import urlencode

import requests
from allure_commons.types import AttachmentType

from config.settings import settings
from models.test_user import TestUser
from tools.allure.attach import attach_content


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

    attach_content(
        content=json.dumps(user_data_for_create, indent=4, ensure_ascii=False),
        name='User creation data',
        attachment_type=AttachmentType.JSON
    )
    attach_content(
        content=json.dumps(response.json(), indent=4, ensure_ascii=False),
        name='Create User Response',
        attachment_type=AttachmentType.JSON
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

    attach_content(
        content=json.dumps(user_data_for_delete, indent=4, ensure_ascii=False),
        name='User deletion data',
        attachment_type=AttachmentType.JSON
    )
    attach_content(
        content=json.dumps(response.json(), indent=4, ensure_ascii=False),
        name='Delete User Response',
        attachment_type=AttachmentType.JSON
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
