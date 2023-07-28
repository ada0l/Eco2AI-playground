from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    model_config = SettingsConfigDict(extra="ignore", env_prefix="PLAYGROUND_")
    DATABASE_URL: str
    DATABASE_URL_FOR_MIGRATE: str
    REDIS_URL: str


settings = Settings()
