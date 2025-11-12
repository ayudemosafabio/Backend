from fastapi import WebSocket

from app import authsysfa, config
from app.expection.catch_group.workspace_catch_group_exception import workspace_exception
from app.integration.ai_workspace_integration import AIWorkspaceIntegration
from app.service.user_chat_service import UserChatService


class AIWorkspaceController:

    __slots__ = ("__client", "__integration", "__service")

    def __init__(self) -> None:
        self.__service = UserChatService(authsysfa().crud_by_role) #type:ignore
        self.__integration = AIWorkspaceIntegration(config)

    @workspace_exception
    async def chat_AI(self, websocket: WebSocket, **actions):
        async with self.__integration() as client:
            while True:
                await self.__service.chat_AI(websocket, client, **actions)
    
    @workspace_exception
    async def private_chat_between_users(self, websocket: WebSocket,user_id: str, user_name: str):
        active_users: dict[str, dict] = {}
        active_users[user_id] = {"name": user_name, "socket": websocket}

        while True:
            await self.__service.private_chat_between_users()

    @workspace_exception
    async def public_chat(self, websocket: WebSocket,user_id: str, user_name: str):
        active_users: dict[str, dict] = {}
        active_users[user_id] = {"name": user_name, "socket": websocket}

        while True:
            await self.__service.public_chat()

    @workspace_exception
    async def chat_group(self, websocket: WebSocket,user_id: str, user_name: str):
        active_users: dict[str, dict] = {}
        active_users[user_id] = {"name": user_name, "socket": websocket}

        while True:
            await self.__service.public_chat()
   
    @workspace_exception
    async def list_files(self):
        return await self.__integration.list_files()
    
    @workspace_exception
    async def load(self):
        return await self.__integration.list_files()
    
    @workspace_exception
    async def create_file(self):
        return await self.__integration.list_files()
    
    @workspace_exception
    async def upload_file(self, file_id: str):
        return await self.__integration.upload_file(file_id)
    
    @workspace_exception
    async def delete_file(self, file_id: str):
        return await self.__integration.delete_file(file_id)
    
    @workspace_exception
    async def add_file_to_knowledge(self):
        return await self.__integration.add_file_to_knowledge("")
