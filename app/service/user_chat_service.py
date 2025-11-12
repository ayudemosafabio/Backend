from typing import TYPE_CHECKING, Any, Dict, List

from fastapi import WebSocket

from app.expection.user_chat_exception import InvalidParameter

if TYPE_CHECKING:
    from authsys.core.main.user.crud.async_cbr import Async_cbr
    from httpx import AsyncClient

class UserChatService:


    def __init__(self, database: Async_cbr) -> None:
        self.__database = database
       

    async def private_chat_between_users(self):
        self.__database.create

    async def public_chat(self):
        pass

    async def chat_AI(self, websocket: WebSocket, client: AsyncClient, **actions):
        data = await websocket.receive_json()
        prompt = data.get("prompt")

        payload = self.get_chat_AI_payload("models/gemini-2.5-flash", [{"role": "user", "content": prompt}], **actions)

        async with client.stream(
            "POST",
            "OPENWEBUI_URL",
            json=payload,
            headers={"Authorization": f"Bearer {"API_TOKEN"}"}
        ) as response:
            async for chunk in response.aiter_text():
                await websocket.send_text(chunk)

        await websocket.send_text("[END]")

    def get_chat_AI_payload(self, model: str, messages: List[Dict[str, Any]], **actions):
        att = {"files", ""}
        for action in list(actions.keys()):
            if not action in att: raise InvalidParameter(f"The parameter {action} is invalid")

        return {
            "model" : model,
            "messages": messages,
            **actions
        }




