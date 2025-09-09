from enum import Enum

from pydantic import BaseModel, EmailStr


class Gender(str, Enum):
    MR = "Mr"
    MRS = "Mrs"


class AccountInformation(BaseModel):
    gender: Gender
    name: str
    email: EmailStr
    password: str


class DateOfBirth(BaseModel):
    birth_date: str
    birth_month: str
    birth_year: str


class AddressInformation(BaseModel):
    firstname: str
    lastname: str
    company: str
    address1: str
    address2: str
    country: str
    state: str
    city: str
    zipcode: str
    mobile_number: str


class TestUser(BaseModel):
    __test__ = False

    account_information: AccountInformation
    date_of_birth: DateOfBirth
    address_information: AddressInformation
