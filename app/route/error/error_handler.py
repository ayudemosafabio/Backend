from fastapi import Request, Response, status
from app import app, config

def __check_debug_state(is_debug: Response, is_not_debug: Response):
    return is_debug if config.DEBUG == True else is_not_debug

@app.exception_handler(status.HTTP_405_METHOD_NOT_ALLOWED)
async def method_not_allowed(request: Request, exc):
    return __check_debug_state(
        is_debug = Response(
            status_code=status.HTTP_405_METHOD_NOT_ALLOWED
        ),
        is_not_debug = Response(
            status_code=status.HTTP_502_BAD_GATEWAY
        )
    )

@app.exception_handler(status.HTTP_429_TOO_MANY_REQUESTS)
async def too_many_request(request: Request, exc):
    return __check_debug_state(
        is_debug = Response(
            status_code=status.HTTP_429_TOO_MANY_REQUESTS
        ),
        is_not_debug = Response(
            status_code=status.HTTP_502_BAD_GATEWAY
        )
    )

@app.exception_handler(status.HTTP_409_CONFLICT)
async def conflict(request: Request, exc):
    return __check_debug_state(
        is_debug = Response(
            status_code=status.HTTP_409_CONFLICT
        ),
        is_not_debug = Response(
            status_code=status.HTTP_502_BAD_GATEWAY
        )
    )
     

