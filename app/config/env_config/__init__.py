from typing import Literal

from app.config.env_config.development import Development
from app.config.env_config.production import Production


def set_config(type: Literal["production", "development"] = "development"):
    if type == "development":
        return Development()
    else:
        return Production()