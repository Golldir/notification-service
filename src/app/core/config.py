# src/app/core/config.py
from dynaconf import Dynaconf
from pydantic_settings import BaseSettings

_settings = Dynaconf(
    settings_files=["settings.yaml"],
    envvar_prefix="DYNACONF",
    environments=True,
    default_env="local",
    lowercase_read=True,
)


class Settings(BaseSettings):
    app_name: str
    app_env: str
    db_url: str


settings = Settings(
    app_name="notification-service",
    app_env=_settings.get("app_env", "local"),
    db_url=_settings.get("database.url"),
)
