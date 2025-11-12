from fastapi import APIRouter, Response

cookies_sys = APIRouter(tags=["Cookies"])

@cookies_sys.get("/csrf")
def cookies(response: Response):
    return response.set_cookie(
        "csrf",
        "__token__"
    )


