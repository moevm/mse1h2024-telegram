from pydantic import (
    MongoDsn,
    AmqpDsn,
    computed_field
)
from pydantic_core import MultiHostUrl
from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    model_config = SettingsConfigDict(
        env_file=('.env', '.env.prod'),
        env_ignore_empty=True,
        extra="ignore"
    )

    GDRIVE_API_CREDENTIALS: str
    TELEGRAM_BOT_TOKEN: str


    MONGO_DB: str
    MONGO_HOST: str
    MONGO_PORT: int = 27017
    MONGO_USER: str
    MONGO_PASS: str

    @computed_field
    @property
    def MONGO_DB_URI(self) -> MongoDsn:
        return MultiHostUrl.build(
            scheme="mongodb",
            host=self.MONGO_HOST,
            username=self.MONGO_USER,
            password=self.MONGO_PASS,
            port=self.MONGO_PORT
        )


    RABBITMQ_USER: str
    RABBITMQ_PASS: str
    RABBITMQ_HOST: str

    @computed_field
    @property
    def RABBIT_URI(self) -> AmqpDsn:
        return MultiHostUrl.build(
            scheme="amqp",
            host=self.RABBITMQ_HOST,
            username=self.RABBITMQ_USER,
            password=self.RABBITMQ_PASS
        )


settings = Settings()