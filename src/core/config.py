from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    model_config = SettingsConfigDict(
        env_file=".env",
        env_ignore_empty=True,
        extra="ignore",
    )

    # === Database ===
    DATABASE_URL: str = (
        "mssql+pyodbc://sa:YourStrongPassword123!@localhost:1433/agro_platform"
        "?driver=ODBC+Driver+18+for+SQL+Server"
        "&TrustServerCertificate=yes"
        "&Encrypt=no"
    )

    # === Security ===
    SECRET_KEY: str = "CHANGE_THIS_TO_A_VERY_LONG_RANDOM_SECRET_IN_PRODUCTION_2026"
    ALGORITHM: str = "HS256"
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 60 * 24 * 7  # 7 дней

    # === Application ===
    PROJECT_NAME: str = "Агро Платформа"


settings = Settings()
