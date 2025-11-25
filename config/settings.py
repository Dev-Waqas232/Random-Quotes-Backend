from pydantic_settings import BaseSettings, SettingsConfigDict
from dotenv import load_dotenv

load_dotenv()


class Settings(BaseSettings):
    QUOTE_URL: str
    PORT: int

    model_config = SettingsConfigDict(env_file=".env", extra="ignore")


settings = Settings()
