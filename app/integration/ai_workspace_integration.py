from http import HTTPMethod
from typing import Union, TYPE_CHECKING
from urllib.parse import urljoin

from app.integration.shared.base_integration import BaseIntegration

if TYPE_CHECKING:
    from app.config.env_config import Development, Production

class AIWorkspaceIntegration(BaseIntegration):

    def __init__(self, config: Union[Development, Production]) -> None:
        super().__init__(config.WORKSPACE_URL)

    async def list_files(self, method=HTTPMethod.GET, endpoint="api/v1/files/"):
        return await self._client.get(urljoin(self._base_url, "api/v1/files/"))

    async def upload_file(self, value: str, method=HTTPMethod.POST, endpoint="api/v1/files/", **data):
        return await self._client.post(urljoin(self._base_url, "api/v1/files/"))

    async def delete_file(self, value: str, method=HTTPMethod.DELETE, endpoint="api/v1/files/"): 
        return await self._client.delete(urljoin(self._base_url, "api/v1/files/"))

    async def list_knowledge(self, method=HTTPMethod.GET, endpoint="api/v1/knowledge/"):
        return await self._client.get(urljoin(self._base_url, "api/v1/files/"))
    
    async def create_knowledge(self, method=HTTPMethod.POST, endpoint="api/v1/knowledge/", **data):
        return await self._client.post(urljoin(self._base_url, "api/v1/files/"))
    
    async def add_file_to_knowledge(self, endpoint: str, method=HTTPMethod.POST, **data):
        return await self._client.post(urljoin(self._base_url, "api/v1/files/"))
    

    
