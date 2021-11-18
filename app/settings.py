from pydantic import BaseSettings


class AppSettings(BaseSettings):
    """Main settings."""

    class Config:
        env_file = ".env"

    SECRET_KEY: str
    ALGORITHM: str = "HS256"
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 30
    POSTGRES_DSN: str


config = AppSettings()
