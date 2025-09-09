from pydantic import HttpUrl, BaseModel, FilePath, EmailStr, PaymentCardNumber, Field, DirectoryPath
from pydantic_settings import BaseSettings, SettingsConfigDict
from typing_extensions import Self


class TestData(BaseModel):
    image_file: FilePath
    counter_file: FilePath


class PaymentCardInfo(BaseModel):
    name: str
    number: PaymentCardNumber
    cvc: int = Field(..., ge=100, le=999)
    expiry_month: str
    expiry_year: int


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
    artifacts_dir: DirectoryPath
    downloads_dir: DirectoryPath
    tracing_dir: DirectoryPath

    payment_card_info: PaymentCardInfo

    @classmethod
    def initialize(cls) -> Self:
        browser_state_file = FilePath('browser-state.json')
        browser_state_file.touch(exist_ok=True)

        artifacts_dir = DirectoryPath('./artifacts')
        artifacts_dir.mkdir(exist_ok=True)

        downloads_dir = DirectoryPath('./artifacts/downloads')
        downloads_dir.mkdir(exist_ok=True)

        tracing_dir = DirectoryPath('./artifacts/tracing')
        tracing_dir.mkdir(exist_ok=True)

        return Settings(
            browser_state_file=browser_state_file,
            artifacts_dir=artifacts_dir,
            downloads_dir=downloads_dir,
            tracing_dir=tracing_dir
        )

    def get_base_url(self) -> str:
        return f"{self.app_url}"


settings = Settings.initialize()
