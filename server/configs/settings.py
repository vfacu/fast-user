from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    # API
    PORT: int = 8080
    DEV: bool = False

    # External Data
    USERS_API: str

    # Database
    DB_CONN: str

    # Logging
    DEBUG: bool = False

    class Config:
        env_file = '.env'
