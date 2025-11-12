import hashlib
from fastapi import Request


def get_client_fingerprint(request: Request) -> str:
    ip = request.client.host or "_N/A_"  # type:ignore
    user_agent = request.headers.get("user-agent", "")
    accept_lang = request.headers.get("accept-language", "")
    forwarded_for = request.headers.get("x-forwarded-for", "")
    raw_data = f"{ip}|{user_agent}|{accept_lang}|{forwarded_for}"
    return hashlib.sha256(raw_data.encode("utf-8")).hexdigest()