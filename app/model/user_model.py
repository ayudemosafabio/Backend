from uuid import UUID, uuid4
from sqlmodel import Field, SQLModel


class Users(SQLModel, table=True):
    user_id: UUID = Field(primary_key=uuid4())
    name: str
    last_name: str
    where_from: str
    professional_id: str
    