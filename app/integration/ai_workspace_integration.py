from typing import Union, TYPE_CHECKING
from urllib.parse import urljoin

from app.integration.shared.base_integration import BaseIntegration

if TYPE_CHECKING:
    from app.config.env_config import Development, Production

class AIWorkspaceIntegration(BaseIntegration):

    def __init__(self, config: Union[Development, Production]) -> None:
        super().__init__(config.WORKSPACE_URL)

    async def list_files(self):
        return await self._client.get(urljoin(self._base_url, "api/v1/files/"))

    async def upload_file(self, file_id: str):
        return await self._client.post(urljoin(self._base_url, "api/v1/files/"))

    async def delete_file(self, file_id: str): 
        return await self._client.delete(urljoin(self._base_url, "api/v1/files/"))

    async def list_knowledge(self):
        return await self._client.get(urljoin(self._base_url, "api/v1/files/"))
    
    async def create_knowledge(self):
        return await self._client.post(urljoin(self._base_url, "api/v1/files/"))
    
    async def add_file_to_knowledge(self):
        return await self._client.post(urljoin(self._base_url, "api/v1/files/"))
    

    
