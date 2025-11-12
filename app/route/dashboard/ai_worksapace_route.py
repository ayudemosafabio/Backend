from fastapi import APIRouter, Depends, WebSocket

from app.controller.dashboard.ai_worksapace_controller import AIWorkspaceController

ai_workspace = APIRouter(prefix="/workspace", tags=['Chat'], )
controller = AIWorkspaceController()

@ai_workspace.websocket("/ia_chat/")
async def ai_chat(websocket: WebSocket):
    await websocket.accept()
    return await controller.chat_AI(websocket)

@ai_workspace.websocket("/user_chat/")
async def user_chat(websocket: WebSocket):
    await websocket.accept()
    return await controller.private_chat_between_users(websocket, "", "")

