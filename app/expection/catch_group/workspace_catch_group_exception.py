from functools import wraps
from fastapi import WebSocket

from app.expection.error_exception import Error

def chat_workspace_exception(func):
    @wraps(func)
    async def catcher(*args, **kwargs):
        websocket = None
        for arg in args:
            if isinstance(arg, WebSocket):
                websocket = arg
                break

        try:
            return await func(*args, **kwargs)
        except Exception as e:
            error_message = f"[workspace_exception] {type(e).__name__}: {str(e)}"
            if websocket and not websocket.client_state.name == "DISCONNECTED":
                try:
                    await websocket.send_text(error_message)
                except Exception:
                    pass
                finally:
                    await websocket.close(code=1011)
        finally:
            for arg in args:
                if hasattr(arg, "_client"):
                    client = getattr(arg, "_client")
                    if hasattr(client, "aclose"):
                        await client.aclose()

    return catcher

def workspace_exception(func):
    @wraps(func)
    async def catcher(*args, **kwargs):
        try:
            return await func(*args, **kwargs)
        except:
            raise Error(500, detail="chatcher group")
    return catcher
