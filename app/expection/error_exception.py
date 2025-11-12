from http import HTTPStatus
from typing import Dict, Optional, Union
from fastapi import HTTPException

from app.provider.request.request import request

class Error(HTTPException):

    def __init__(self, 
        status_code:Union[int, HTTPStatus], 
        detail: str = "It shouldn't be here", 
        headers: Optional[Dict[str, str]] = None, 
        block_client: bool = False,
    ):
        if block_client==True:
            from app import config
            self.__block_client(message=detail)
            if config.DEBUG==False:
                detail = ""
        if not isinstance(status_code, int): status_code = status_code.value
        super().__init__(status_code=status_code, detail=detail, headers=headers)


    def __block_client(self, message: str):
        _request = request()
        _request.state.block_client = True
        _request.state.block_message = message


