from typing import Union, TYPE_CHECKING
from httpx import AsyncClient

if TYPE_CHECKING:
    from app.config.env_config import Development, Production

class BaseIntegration:

    __slots__ = ("_base_url", "_client")

    def __init__(self, url: str) -> None:
        self._base_url: str = url
        self._client = AsyncClient(http2=True, base_url=self._base_url, timeout=30.0)

    def __call__(self) -> AsyncClient:
        return self._client