from os import getenv

from app.config.env_config.config import Config


class Production(Config):
    HOST = getenv("HOST", "localhost")
    PORT = int(getenv("PORT", 5000))
    DEBUG = False
    LOG_LEVEL = getenv("LOG_LEVEL", "info")
    RELOAD = bool(getenv("RELOAD"))
    DOCS_URL = None
    REDOC_URL = None
    OPENAPI_URL = None

    REDIS_REATE_LIMIT = getenv("REDIS_REATE_LIMIT", "redis://localhost:6379/0")

    DATABASE = getenv("DATABASE", "redis://localhost:6379/0")
    ECHO_DATABASE = False