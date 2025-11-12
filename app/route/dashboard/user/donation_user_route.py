from fastapi import APIRouter, Depends

from app.controller.dashboard.user.donation_user_controller import DonationUserController


donation_user = APIRouter(prefix="/user_info_donation", tags=['User info donations'])
controller = DonationUserController()

@donation_user.post("/create_donation/")
async def create_donation():
    return 

@donation_user.get("/get_all_donation/")
async def get_all_donations():
    return 

@donation_user.get("/get_donation/")
async def get_donations():
    return 



