from uuid import uuid4
from krelego import AsyncKrelego

from app.infrastructure.donation_schema import DonationCreate
from app.model.donation_model import Donation


class InvoiceService:

    def __init__(self, database: AsyncKrelego) -> None:
        self.__database = database

    async def get_all_invoices(self):
        pass

    async def get_invoice(self):
        pass
