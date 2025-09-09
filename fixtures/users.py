import pytest

from data.test_users import get_test_user
from models.test_user import TestUser
from tools.api.api_client import create_user_account, delete_user_account, is_user_exists


@pytest.fixture
def authorized_test_user() -> TestUser:
    test_user = get_test_user()
    create_user_account(test_user)

    yield test_user

    delete_user_account(test_user)


@pytest.fixture
def new_test_user() -> TestUser:
    test_user = get_test_user()

    yield test_user

    if is_user_exists(test_user):
        delete_user_account(test_user)


