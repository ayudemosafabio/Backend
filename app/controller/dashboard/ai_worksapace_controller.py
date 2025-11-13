from fastapi import WebSocket

from app import authsysfa, config
from app.expection.catch_group.workspace_catch_group_exception import chat_workspace_exception, workspace_exception
from app.integration.ai_workspace_integration import AIWorkspaceIntegration
from app.service.chat.user_chat_service import UserChatService


class AIWorkspaceController:

    __slots__ = ("__client", "__service")

    def __init__(self) -> None:
        self.__service = UserChatService(authsysfa().crud_by_role) #type:ignore
        self.__client = AIWorkspaceIntegration(config)

    @chat_workspace_exception
    async def AI_chat(self, websocket: WebSocket, **actions):
        async with self.__client as client:
            while True:
                await self.__service.chat_AI(websocket, client, **actions)
    
    @chat_workspace_exception
    async def private_chat_between_users(self, websocket: WebSocket, user_id: str, user_name: str):
        active_users: dict[str, dict] = {}
        active_users[user_id] = {"name": user_name, "socket": websocket}

        while True:
            await self.__service.private_chat_between_users()

    @chat_workspace_exception
    async def public_chat(self, websocket: WebSocket,user_id: str, user_name: str):
        active_users: dict[str, dict] = {}
        active_users[user_id] = {"name": user_name, "socket": websocket}

        while True:
            await self.__service.public_chat()

    @chat_workspace_exception
    async def chat_group(self, websocket: WebSocket,user_id: str, user_name: str):
        active_users: dict[str, dict] = {}
        active_users[user_id] = {"name": user_name, "socket": websocket}

        while True:
            await self.__service.public_chat()
   
    @workspace_exception
    async def list_files(self):
        response = await self.__client.list_files()
        await self.__client().aclose()
        return response
    
    @workspace_exception
    async def load(self):
        return await self.__client.list_files()
    
    @workspace_exception
    async def create_file(self):
        return await self.__client.list_files()
    
    @workspace_exception
    async def upload_file(self, file_id: str):
        return await self.__client.upload_file(file_id)
    
    @workspace_exception
    async def delete_file(self, file_id: str):
        response = await self.__client.delete_file(file_id)
        await self.__client().aclose()
        return response
    
    @workspace_exception
    async def add_file_to_knowledge(self):
        return await self.__client.add_file_to_knowledge()
