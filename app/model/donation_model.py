from uuid import UUID, uuid4
from sqlmodel import Field, SQLModel


class Donation(SQLModel, table=True):
    donation_id: UUID = Field(primary_key=uuid4())