from typing import Union
from uuid import UUID, uuid4
from pydantic import BaseModel, SecretStr, field_validator
from authsys import SafeField, CheckSafeField


class UserSchema(BaseModel):
    user_id: Union[UUID, SafeField] = uuid4()
    role: str
    name: str
    last_name: str
    where_from: str
    professional_id: str

    @field_validator("user_id", mode="before")
    @classmethod
    def convert_uuid_to_safefield(cls, v):
        if isinstance(v, SafeField):
            return v
        if isinstance(v, (UUID, str)):
            return SafeField(value=SecretStr(str(v)))
        raise TypeError("user_id must be UUID or valid SafeField.")

class LoginSchema(BaseModel):
    user_id: Union[UUID, CheckSafeField]

    @field_validator("user_id", mode="before")
    @classmethod
    def convert_uuid_to_checksafefield(cls, v):
        if isinstance(v, CheckSafeField):
            return v
        if isinstance(v, (UUID, str)):
            return CheckSafeField(value=SecretStr(str(v)))
        raise TypeError("user_id must be UUID or valid CheckSafeField.")




    