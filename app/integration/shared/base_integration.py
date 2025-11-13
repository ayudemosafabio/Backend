from httpx import AsyncClient

class BaseIntegration:
    __slots__ = ("_base_url", "_client")

    def __init__(self, url: str, api_key: str) -> None:
        self._base_url = url
        self._client = AsyncClient(
            base_url=self._base_url, 
            timeout=30.0,
            headers={
                "Authorization": f"Bearer {api_key}",
                "Content-Type": "application/json"
            }
        )
        

    def __call__(self) -> AsyncClient:
        return self._client

    async def __aenter__(self):
        return self._client

    async def __aexit__(self, exc_type, exc_val, exc_tb):
        await self._client.aclose()
