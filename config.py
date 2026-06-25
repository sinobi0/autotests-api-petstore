from pydantic import BaseModel, FilePath, DirectoryPath
from pydantic_settings import SettingsConfigDict, BaseSettings

class HTTPClientConfig(BaseModel):
    """
    Модель с настройками http-клиента
    """
    url: str
    timeout: float

    @property
    def client_url(self) -> str:
        """
        :return: Возвращает обычную строку url для httpx
        """
        return str(self.url)

class TestDataConfig(BaseModel):
    image_file: FilePath


class Settings(BaseSettings):
    model_config = SettingsConfigDict(
        extra='allow',
        env_file=".env",
        env_file_encoding="utf-8",
        env_nested_delimiter=".",
    )
    test_data: TestDataConfig
    http_client: HTTPClientConfig
    allure_results_dir: DirectoryPath

    @classmethod
    def initialize(cls):
        allure_results_dir = DirectoryPath("./allure-results")
        allure_results_dir.mkdir(exist_ok=True)

        return cls(allure_results_dir=allure_results_dir)

settings = Settings.initialize()
