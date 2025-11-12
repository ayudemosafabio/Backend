from typing import List, Union
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.utils.cors.config import CORSConfig
from app.utils.cors.types import CORSType



class CORSManager:
    """Gestor de CORS para aplicaciones FastAPI"""
    
    @staticmethod
    def apply(app: FastAPI, cors_type: CORSType, **kwargs) -> FastAPI:
        """
        Aplicar configuración CORS a una aplicación FastAPI
        
        Args:
            app: Aplicación FastAPI
            cors_type: Tipo de configuración CORS
            **kwargs: Argumentos adicionales específicos para cada configuración
            
        Returns:
            FastAPI: La aplicación con el middleware CORS configurado
        """
        config = CORSManager._get_config(cors_type, **kwargs)
        app.add_middleware(
            CORSMiddleware,
            **config.as_dict()
        )
        return app
    
    @staticmethod
    def _get_config(cors_type: CORSType, **kwargs) -> CORSConfig:
        """Obtener la configuración CORS según el tipo"""
        match cors_type:
            case CORSType.CORS:
                return CORSConfig(**kwargs)
            case CORSType.PUBLIC_API:
                return CORSConfig.public_api(origins=kwargs.get('origins'))
            case CORSType.PRIVATE_API:
                return CORSConfig.private_api(origins=kwargs.get('origins'))
            case CORSType.FRONTEND:
                return CORSConfig.frontend(domain=kwargs['domain'])
            case CORSType.FRONTEND_PUBLIC_API:
                return CORSConfig.frontend_public_api(domain=kwargs['domain'])
            case CORSType.FRONTEND_PRIVATE_API:
                return CORSConfig.frontend_private_api(domain=kwargs['domain'])
            case CORSType.FRONTEND_SUBDOMAIN:
                return CORSConfig.frontend_subdomain(domain=kwargs['domain'], subdomains=kwargs['subdomains'])
            case CORSType.FRONTEND_SUBDOMAIN_PUBLIC_API:
                return CORSConfig.frontend_subdomain_public_api(domain=kwargs['domain'], subdomains=kwargs['subdomains'])
            case CORSType.FRONTEND_SUBDOMAIN_PRIVATE_API:
                return CORSConfig.frontend_subdomain_private_api(domain=kwargs['domain'], subdomains=kwargs['subdomains'])
            case CORSType.FRONTEND_PP:
                return CORSManager._handle_pp_config(
                    domain=kwargs['domain'],
                    public_routes=kwargs['public_routes'],
                    private_routes=kwargs['private_routes']
                )
            case CORSType.FRONTEND_SUBDOMAIN_PP:
                return CORSManager._handle_subdomain_pp_config(
                    domain=kwargs['domain'],
                    subdomains=kwargs['subdomains'],
                    public_routes=kwargs['public_routes'],
                    private_routes=kwargs['private_routes']
                )
            case _:
                raise ValueError(f"Tipo de CORS no válido: {cors_type}")
    
    @staticmethod
    def _handle_pp_config(domain: str, public_routes: List[str], private_routes: List[str]) -> CORSConfig:
        """
        Manejar configuración de rutas públicas y privadas para FastAPI
        
        Nota: En FastAPI, a diferencia de Flask, no podemos aplicar diferentes configuraciones CORS
        a diferentes rutas usando el middleware estándar. Retornamos una configuración que 
        satisfaga los requisitos de ambos tipos de rutas.
        """
        # Para FastAPI, debemos aplicar una configuración única que satisfaga todos los requisitos
        # En este caso, usaremos la configuración más permisiva (la privada)
        return CORSConfig.frontend_private_api(domain=domain)
    
    @staticmethod
    def _handle_subdomain_pp_config(
        domain: str, 
        subdomains: List[str], 
        public_routes: List[str], 
        private_routes: List[str]
    ) -> CORSConfig:
        """Manejar configuración de rutas públicas y privadas para subdominios"""
        # Similar al caso anterior, aplicamos la configuración más permisiva
        return CORSConfig.frontend_subdomain_private_api(domain=domain, subdomains=subdomains)


def setup_cors(app: FastAPI, cors_type: Union[CORSType, str], **kwargs) -> FastAPI:
    """
    Configurar CORS para una aplicación FastAPI
    
    Args:
        app: Aplicación FastAPI
        cors_type: Tipo de configuración CORS (puede ser un valor de enum o string)
        **kwargs: Argumentos adicionales para la configuración
        domain: str = "",
        origins: Sequence[str] = (),
        allow_methods: Sequence[str] = ("GET",),
        allow_headers: Sequence[str] = (),
        allow_credentials: bool = False,
        allow_origin_regex: str | None = None,
        expose_headers: Sequence[str] = (),
        max_age: int = 600,
            
    Returns:
        FastAPI: La aplicación con el middleware CORS configurado
    """
    # Convertir string a enum si es necesario
    if isinstance(cors_type, str):
        cors_type = CORSType(cors_type)
    
    return CORSManager.apply(app, cors_type, **kwargs)

