from uuid import UUID
from fastapi import Request
from authsys import Custom_verification, ReCaptcha, A2fRegister
from authsysfa import AsyncAuthsysFA, InfoUser, TwoFactorData, get_a2f_values_from_env
from authlib.integrations.starlette_client import OAuth, OAuthError

from app.infrastructure.user_schema import LoginSchema, UserSchema
from app.integration.check_user_integration import Check_user_integration


class AuthController:

    def __init__(self, authsysfa: AsyncAuthsysFA) -> None:
        self.__authsysfa = authsysfa
        self.__OAuth = OAuth()
        self.__reCaptcha = ReCaptcha(
            sitekey="", 
            url="",
        )

        self.__check_user = Check_user_integration()

        self.__OAuth.register(
            name='google',
            server_metadata_url='https://accounts.google.com/.well-known/openid-configuration',
            client_id="",
            client_secret="",
            client_kwargs={
                'scope': 'openid',
                'redirect_uri': 'http://localhost:5000/auth'
            }
        )

    async def register_user(self, request: Request, schema: UserSchema):
       self.__reCaptcha.url = ""
       return await self.__authsysfa().public_create_user.register_user(
           field_name_id="user_id", ip=request.client.host, user_agent=request.headers.get("user-agent"), #type:ignore
           get_by={"user_id", "user_name"}, schema=schema, custom_verification=Custom_verification(
               handler=self.__check_user.check_user, args=()
           ), 
           reCaptcha=self.__reCaptcha
       )

    async def login(self, request: Request, schema: LoginSchema):
        self.__reCaptcha.url = ""
        return await self.__authsysfa().auth.login(
            field_name_id="user_id",  get_by="user_id", compare_fields={"user_id", "is_active"},
            schema=schema, ip=request.client.host, user_agent=request.headers.get("user-agent"), custom_verification=Custom_verification( #type:ignore
                handler=self.__OAuth.google.authorize_redirect, #type:ignore
                args=(request, request.url_for('auth_callback'))
            ),
            reCaptcha=self.__reCaptcha
        )
    
    async def a2f(self, code: TwoFactorData, secure_data: InfoUser):
        self.__reCaptcha.url = ""
        company, digest, _, digits, __, interval  = get_a2f_values_from_env(self.__authsysfa.config)  
        return await self.__authsysfa().auth.a2f_login(str(code.code), A2fRegister(
            user_id=UUID(secure_data.user_id),
            user_name=secure_data.user_name,
            company_name=company,
            digest=digest,
            digits=digits, #type:ignore
            interval=interval
        ), reCaptcha=self.__reCaptcha)

    def logout(self, request: Request):
        return request.url_for("/logout")

    