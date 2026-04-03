from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    model_config = SettingsConfigDict(
        env_file=".env",
        env_ignore_empty=True,
        extra="ignore",
    )

    # === Database ===
    DATABASE_URL: str

    # === Security ===
    SECRET_KEY: str
    ALGORITHM: str = "HS256"
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 60 * 24 * 7  # 7 дней

    # === Application ===
    PROJECT_NAME: str = "Агро Платформа"


settings = Settings()  # pyright: ignore[reportCallIssue]
