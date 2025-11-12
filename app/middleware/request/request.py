from contextvars import ContextVar
from fastapi import Request
from starlette.middleware.base import BaseHTTPMiddleware

_request_context: ContextVar[Request] = ContextVar("request")

class Request_context(BaseHTTPMiddleware):
    async def dispatch(self, request: Request, call_next):
        token = _request_context.set(request)
        try:
            response = await call_next(request)
            return response
        finally:
            _request_context.reset(token)
