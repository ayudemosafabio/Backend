from fastapi import FastAPI
from authsysfa import AsyncAuthsysFA

from app.middleware import init_middlewares
from app.model.user_model import Users
from app.utils.cors.cors import setup_cors
from app.utils.cors.types import CORSType
from app.utils.init_lifespan import init_lifespan

# ====================== Config ======================
from app.config import set_config
config = set_config()

# ====================== App ======================
app = FastAPI(
    title=config.APP_NAME,
    description=config.DESCRIPTION,
    version=config.VERSION,
    docs_url=config.DOCS_URL,
    redoc_url=config.REDOC_URL,
    openapi_url=config.OPENAPI_URL,
    lifespan=init_lifespan(config),
    middleware=init_middlewares()
)

# ====================== Cors ======================
setup_cors(
    app, 
    CORSType.PRIVATE_API,
    origins=["http://localhost:4321"], 
    allow_credentials=True,
    allow_headers=[],
    allow_origin_regex=None,
    expose_headers=["X-CSRF-Token"],
    max_age=600
)

# ====================== Authsys ======================
authsysfa = AsyncAuthsysFA(app)
authsysfa.init_app(
    user_model=Users, 
    add_routes=True, 
    ratelimit=True, 
    auth_router=False, 
    register_user_router=False,
)

# ====================== Routes ======================
from app.route import include_package_routers
include_package_routers(app, "app.route")