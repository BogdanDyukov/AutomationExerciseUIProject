from models.test_user import TestUser, Title, DateOfBirth, AddressInformation, AccountInformation
from config.settings import settings

new_test_user = TestUser(
    account_information=AccountInformation(
        title=Title.MR,
        name=settings.new_test_user_username,
        email=settings.new_test_user_email,
        password=settings.new_test_user_password
    ),
    date_of_birth=DateOfBirth(
        birth_date="15",
        birth_month="8",
        birth_year="1990"
    ),
    address_information=AddressInformation(
        firstname="John",
        lastname="Doe",
        company="Acme Corp",
        address1="123 Main St",
        address2="Apt 4",
        country="United States",
        state="NY",
        city="New York",
        zipcode="10001",
        mobile_number="1234567890"
    )
)

authorized_test_user = TestUser(
    account_information=AccountInformation(
        title=Title.MR,
        name=settings.authorized_test_user_username,
        email=settings.authorized_test_user_email,
        password=settings.authorized_test_user_password
    ),
    date_of_birth=DateOfBirth(
        birth_date="15",
        birth_month="8",
        birth_year="1990"
    ),
    address_information=AddressInformation(
        firstname="John",
        lastname="Doe",
        company="Acme Corp",
        address1="123 Main St",
        address2="Apt 4",
        country="United States",
        state="NY",
        city="New York",
        zipcode="10001",
        mobile_number="1234567890"
    )
)
