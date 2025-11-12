from enum import Enum


class CORSType(Enum):
    """Tipos de configuración CORS disponibles"""
    CORS = 'cors'
    PUBLIC_API = 'public_api'
    PRIVATE_API = 'private_api'
    FRONTEND = 'frontend'
    FRONTEND_PUBLIC_API = 'frontend_public_api'
    FRONTEND_PRIVATE_API = 'frontend_private_api'
    FRONTEND_SUBDOMAIN = 'frontend_subdomain'
    FRONTEND_SUBDOMAIN_PUBLIC_API = 'frontend_subdomain_public_api'
    FRONTEND_SUBDOMAIN_PRIVATE_API = 'frontend_subdomain_private_api'
    FRONTEND_PP = 'frontend_pp'
    FRONTEND_SUBDOMAIN_PP = 'frontend_subdomain_pp'
