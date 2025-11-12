from os import getenv

from app.config.env_config.config import Config


class Development(Config):
    HOST = getenv("HOST", "localhost")
    PORT = int(getenv("PORT", 5000))
    DEBUG = True
    LOG_LEVEL = "info"
    RELOAD = True
    DOCS_URL = "/docs"
    REDOC_URL = "/redoc"
    OPENAPI_URL = "/openapi.json"

    REDIS_REATE_LIMIT = getenv("REDIS_REATE_LIMIT", "redis://localhost:6379/0")

    DATABASE = getenv("DATABASE", "mysql+asyncmy://root@localhost:3306/krelego")
    ECHO_DATABASE = bool(getenv("ECHO_DATABASE", False))
    