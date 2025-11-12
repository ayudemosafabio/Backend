from fastapi.middleware import Middleware
from krelego import AsyncKrelego, Krelego

from app.middleware.request.request import Request_context
from starlette.middleware.sessions import SessionMiddleware

def init_middlewares():
    return [
        Middleware(Request_context),
        Middleware(SessionMiddleware, secret_key="add any string..."),
    ]