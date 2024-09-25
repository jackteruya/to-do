from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    model_config = SettingsConfigDict(
        env_file=(".env", ".env.test"), env_file_encoding="utf-8"
    )
    db_url: str

    url_prefix: str = ""


settings = Settings()

__all__ = ["settings"]
