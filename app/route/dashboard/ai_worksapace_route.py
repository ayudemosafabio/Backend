from fastapi import APIRouter, Depends, WebSocket

from app.controller.dashboard.ai_worksapace_controller import AIWorkspaceController

ai_workspace = APIRouter(prefix="/workspace", tags=['Chat'])

def controller():
    return AIWorkspaceController()

@ai_workspace.websocket("/ia_chat")
async def AI_chat(websocket: WebSocket, controller: AIWorkspaceController = Depends(controller)):
    await websocket.accept()
    return await controller.AI_chat(websocket)

@ai_workspace.websocket("/user_chat")
async def user_chat(websocket: WebSocket):
    await websocket.accept()
    return await AIWorkspaceController().private_chat_between_users(websocket, "", "")

@ai_workspace.get("/list_files")
async def list_files():
    return await AIWorkspaceController().list_files()

@ai_workspace.get("/delete_file/{file_id}")
async def delete_file(file_id: str):
    return await AIWorkspaceController().delete_file(file_id)

