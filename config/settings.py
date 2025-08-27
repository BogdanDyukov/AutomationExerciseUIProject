from pydantic import HttpUrl, BaseModel, FilePath, EmailStr
from pydantic_settings import BaseSettings, SettingsConfigDict
from typing_extensions import Self


class TestData(BaseModel):
    image_file: FilePath


class Settings(BaseSettings):
    model_config = SettingsConfigDict(
        env_file="./.env",  # Указываем, из какого файла читать настройки
        env_file_encoding="utf-8",  # Указываем кодировку файла
        env_nested_delimiter=".",  # Указываем разделитель для вложенных переменных
    )

    app_url: HttpUrl
    headless: bool
    test_data: TestData
    browser_state_file: FilePath

    new_test_user_username: str
    new_test_user_email: EmailStr
    new_test_user_password: str

    authorized_test_user_username: str
    authorized_test_user_email: EmailStr
    authorized_test_user_password: str

    @classmethod
    def initialize(cls) -> Self:
        browser_state_file = FilePath('browser-state.json')
        browser_state_file.touch(exist_ok=True)

        return Settings(
            browser_state_file=browser_state_file
        )

    def get_base_url(self) -> str:
        return f"{self.app_url}"


settings = Settings.initialize()
