import pytest

from data.test_users import authorized_test_user
from tools.api.api_client import create_user_account, delete_user_account


@pytest.fixture(scope='session', autouse=True)
def session_user():
    create_user_account(test_user=authorized_test_user)
    yield
    delete_user_account(test_user=authorized_test_user)
