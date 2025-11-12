from uuid import UUID
from pydantic import BaseModel


class DonationCreate(BaseModel):
    donation_id: UUID
    user_id: UUID