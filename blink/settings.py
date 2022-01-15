from pydantic import BaseSettings

class AppSettings(BaseSettings):
    APP_NAME: str = "blinked"
    DEBUG: bool = True

class ServerSettings(BaseSettings):
    HOST: str = "0.0.0.0"
    PORT: int = 8000

class DatabaseSettings(BaseSettings):
    DB_URI: str
    DB_NAME: str = "blinked"

class SecuritySettings(BaseSettings):
    SECRET_KEY: str
    ALGORITHM = "HS256"
    ACCESS_TOKEN_EXPIRE_MINUTES = 30


class Settings(AppSettings, ServerSettings, DatabaseSettings, SecuritySettings):
    pass



settings = Settings(_env_file='.env')
