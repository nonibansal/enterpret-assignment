import os
from abc import ABC
from typing import Dict, Any
from functools import lru_cache
from pydantic.fields import FieldInfo
from configparser import ExtendedInterpolation, RawConfigParser
from pydantic_settings import BaseSettings, PydanticBaseSettingsSource

here = os.path.abspath(os.path.dirname(__file__))
config_ini_path = os.path.join(here, "config.ini")
dotenv_path = os.path.join(here, "../../.env")


class ConfigINISettingsSource(PydanticBaseSettingsSource, ABC):
    """
    Loads environment variables from env file
    """

    def get_field_value(self, field: FieldInfo, field_name: str) -> tuple[Any, str, bool]:

        env = "local"
        config = RawConfigParser(interpolation=ExtendedInterpolation(), default_section="default")
        config.optionxform = lambda option: option

        config.read(config_ini_path)

        env_settings = dict(**config["default"], **config[env])

        field_value = env_settings.get(field_name)
        return field_value, field_name, False

    def prepare_field_value(self, field_name: str, field: FieldInfo, value: Any, value_is_complex: bool) -> Any:
        return value

    def __call__(self, *args, **kwargs) -> Dict[str, Any]:
        d: Dict[str, Any] = {}

        for field_name, field in self.settings_cls.model_fields.items():
            field_value, field_key, value_is_complex = self.get_field_value(field, field_name)
            field_value = self.prepare_field_value(field_name, field, field_value, value_is_complex)
            if field_value is not None:
                d[field_key] = field_value

        return d


class Settings(BaseSettings):
    ENVIRONMENT: str
    PYTHONPATH: str

    FASTAPI_SERVICE_NAME: str
    FASTAPI_PORT_MODEL_EXECUTOR: str
    # FASTAPI_PORT_MODEL_MANAGEMENT: str
    # FASTAPI_PORT_MODEL_HOSTER: str
    FASTAPI_HOST: str

    PROMETHEUS_PORT: str
    PROMETHEUS_MULTIPROC_DIR: str

    MODEL_MANAGEMENT_URL: str
    MODEL_HOSTER_URL: str

    class Config:
        case_sensitive = True

    @classmethod
    def settings_customise_sources(
        cls,
        settings_cls: type[BaseSettings],
        init_settings: PydanticBaseSettingsSource,
        env_settings: PydanticBaseSettingsSource,
        dotenv_settings: PydanticBaseSettingsSource,
        file_secret_settings: PydanticBaseSettingsSource,
    ) -> tuple[PydanticBaseSettingsSource, ...]:
        return init_settings, env_settings, ConfigINISettingsSource(settings_cls), dotenv_settings, file_secret_settings


@lru_cache()
def get_settings():
    return Settings()

