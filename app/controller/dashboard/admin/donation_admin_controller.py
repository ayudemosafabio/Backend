from typing import Any
from uuid import uuid4

from app import authsysfa
from app.infrastructure.donation_schema import DonationCreate
from app.model.donation_model import Donation
from app.service.invoice_service import InvoiceService


class DonationAdminController:

    def __init__(self) -> None:
        self.__service = InvoiceService(authsysfa().crud_by_role)
        self.__integration = None

    def __call__(self) -> InvoiceService: return self.__service

    async def create_invoice(self):
        self.__service.get_all_invoices

    async def get_all_donation(self):
        pass

    async def get_donation(self):
        pass

    
    
