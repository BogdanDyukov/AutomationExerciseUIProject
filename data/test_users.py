import random

from faker import Faker

from models.test_user import TestUser, Gender, DateOfBirth, AddressInformation, AccountInformation
from tools.counter import get_unique_id

fake = Faker()


def get_test_user() -> TestUser:
    unique_id = get_unique_id()
    fake_birth = fake.date_of_birth()

    return TestUser(
        account_information=AccountInformation(
            gender=random.choice([Gender.MR, Gender.MRS]),
            name=fake.user_name(),
            email=f"user{unique_id}.name@gmail.com",
            password=fake.password(length=8)
        ),
        date_of_birth=DateOfBirth(
            birth_date=str(fake_birth.day),
            birth_month=str(fake_birth.month),
            birth_year=str(fake_birth.year)
        ),
        address_information=AddressInformation(
            firstname=fake.first_name(),
            lastname=fake.last_name(),
            company=fake.company(),
            address1=fake.address(),
            address2=fake.address(),
            country=random.choice(
                ['India', 'United States', 'Canada', 'Australia', 'Israel', 'New Zealand', 'Singapore']
            ),
            state=fake.state(),
            city=fake.city(),
            zipcode=fake.zipcode(),
            mobile_number=fake.phone_number()
        )
    )
