from typing import Any
from uuid import uuid4

from app import database
from app.infrastructure.donation_schema import DonationCreate
from app.model.donation_model import Donation
from app.service.invoice_service import InvoiceService


class DonationAdminController:

    def __init__(self) -> None:
        self.__service = InvoiceService(database)
        self.__integration = None

    def __call__(self) -> InvoiceService: return self.__service

    async def create_invoice(self):
        await database.create(
            get_by = "invoice_id",
            schema = DonationCreate(donation_id = uuid4(), user_id = uuid4()),
            model = Donation
        )

    async def get_all_donation(self):
        pass

    async def get_donation(self):
        pass

    
    
