from html import escape
from typing import Any

def sanitize_value(value: Any) -> Any:
    if isinstance(value, str):
        return escape(value.strip())
    elif isinstance(value, list):
        return [sanitize_value(v) for v in value]
    elif isinstance(value, dict):
        return {k: sanitize_value(v) for k, v in value.items()}
    return value

class Sanitizer:
    @classmethod
    def purge(cls, data: dict, *, remove_none: bool = False) -> dict:
        sanitized = {}
        for k, v in data.items():
            if remove_none and v is None:
                continue
            sanitized[k] = sanitize_value(v)
        return sanitized
