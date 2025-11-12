from pydantic import BaseModel, model_validator

class Safe_base_model(BaseModel):
    @model_validator(mode="before")
    @classmethod
    def auto_sanitize(cls, values: dict) -> dict:
        from app.infrastructure.dto.setting_dto.settings_sys_dto import Sanitizer
        return Sanitizer.purge(values)
