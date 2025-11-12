from fastapi import Request

from app.middleware.request.request import _request_context

def request() -> Request:
    return _request_context.get()