import json
from enum import Enum

from pydantic import HttpUrl, BaseModel, FilePath, PaymentCardNumber, Field, DirectoryPath
from pydantic_settings import BaseSettings, SettingsConfigDict
from typing_extensions import Self


class Browser(str, Enum):
    CHROMIUM = 'chromium'
    FIREFOX = 'firefox'
    WEBKIT = 'webkit'


class TestData(BaseModel):
    image_file: FilePath


class PaymentCardInfo(BaseModel):
    name: str
    number: PaymentCardNumber
    cvc: int = Field(..., ge=100, le=999)
    expiry_month: str
    expiry_year: int


class Settings(BaseSettings):
    model_config = SettingsConfigDict(
        env_file="./config/.env",
        env_file_encoding="utf-8",
        env_nested_delimiter=".",
    )

    app_url: HttpUrl
    headless: bool
    browsers: list[Browser]
    test_data: TestData
    artifacts_dir: DirectoryPath
    counter_file: FilePath
    browser_state_file: FilePath
    allure_results_dir: DirectoryPath
    downloads_dir: DirectoryPath
    tracing_dir: DirectoryPath
    videos_dir: DirectoryPath
    payment_card_info: PaymentCardInfo

    @classmethod
    def initialize(cls) -> Self:
        artifacts_dir = DirectoryPath('./artifacts')
        artifacts_dir.mkdir(exist_ok=True)

        counter_file = FilePath('./artifacts/counter.json')
        counter_file.touch(exist_ok=True)
        counter_file.write_text(json.dumps({"unique_value": 0}))

        browser_state_file = FilePath('./artifacts/browser-state.json')
        browser_state_file.touch(exist_ok=True)
        browser_state_file.write_text('')

        allure_results_dir = DirectoryPath('./allure-results')
        allure_results_dir.mkdir(exist_ok=True)

        downloads_dir = DirectoryPath('./artifacts/downloads')
        downloads_dir.mkdir(exist_ok=True)

        videos_dir = DirectoryPath('./artifacts/videos')
        videos_dir.mkdir(exist_ok=True)

        tracing_dir = DirectoryPath('./artifacts/tracing')
        tracing_dir.mkdir(exist_ok=True)

        return Settings(
            artifacts_dir=artifacts_dir,
            counter_file=counter_file,
            browser_state_file=browser_state_file,
            allure_results_dir=allure_results_dir,
            downloads_dir=downloads_dir,
            videos_dir=videos_dir,
            tracing_dir=tracing_dir
        )

    def get_base_url(self) -> str:
        return f"{self.app_url}"


settings = Settings.initialize()
