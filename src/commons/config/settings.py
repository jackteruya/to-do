from pydantic.v1 import AnyUrl
from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    model_config = SettingsConfigDict(env_file='.env', env_file_encoding='utf-8')
    # postgres_url: AnyUrl
    db_url: str

    url_prefix: str = ""


settings = Settings()

__all__ = ["settings"]
