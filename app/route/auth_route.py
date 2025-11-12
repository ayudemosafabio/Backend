from authsysfa import InfoUser, TwoFactorData
from fastapi import APIRouter, Depends, Request
from fastapi_limiter.depends import RateLimiter

from app import authsysfa
from app.controller import AuthController
from app.infrastructure.user_schema import LoginSchema, UserSchema

auth_router = APIRouter(tags=['Login'])
controller = AuthController(authsysfa)

@auth_router.post('/register_user', dependencies=[Depends(RateLimiter(times=2, seconds=500))])
async def register_user(data: UserSchema, request: Request,):
    return await controller.register_user(request, data)

@auth_router.post('/login', dependencies=[Depends(RateLimiter(times=5, hours=1))])
async def login(data: LoginSchema, request: Request):
    return await controller.login(request, data)

@auth_router.post('/a2f', dependencies=[Depends(RateLimiter(times=5, hours=1))])
async def a2f(code: TwoFactorData, secure_data: InfoUser = Depends(authsysfa().protect_route.protect_a2f)):
    return await controller.a2f(code, secure_data)
    
@auth_router.get('/logout')
async def logout(request: Request):
    return controller.logout(request)

