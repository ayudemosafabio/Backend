from typing import List, Dict, Any, Optional, Set


class CORSConfig:
    """Clase para gestionar configuraciones CORS"""
    
    def __init__(
        self,
        allow_origins: Optional[Set[str]] = None,
        allow_methods: Optional[List[str]] = None,
        allow_headers: Optional[List[str]] = None,
        expose_headers: Optional[List[str]] = None,
        allow_credentials: bool = False,
        max_age: int = 3600
    ):
        self.allow_origins = allow_origins or {"*"}
        self.allow_methods = allow_methods or ["GET", "POST", "PUT", "DELETE", "OPTIONS"]
        self.allow_headers = allow_headers or ["Content-Type", "Authorization", "X-Requested-With", "X-CSRFToken"]
        self.expose_headers = expose_headers or ["Content-Type", "Content-Length", "X-CSRFToken"]
        self.allow_credentials = allow_credentials
        self.max_age = max_age
    
    @classmethod
    def public_api(cls, origins: Optional[List[str]] = None) -> 'CORSConfig':
        """Configuración para API pública"""
        origins_set = set(origins) if origins else {"*"}
        return cls(
            allow_origins=origins_set,
            allow_methods=["GET", "POST", "OPTIONS"],
            allow_headers=["Content-Type", "Authorization", "X-Requested-With"],
            expose_headers=["Content-Type", "Content-Length"],
            allow_credentials=False
        )
    
    @classmethod
    def private_api(cls, origins: Optional[List[str]] = None) -> 'CORSConfig':
        """Configuración para API privada"""
        origins_set = set(origins) if origins else {"http://localhost:3000", "http://127.0.0.1:3000"}
        return cls(
            allow_origins=origins_set,
            allow_credentials=True
        )
    
    @classmethod
    def frontend(cls, domain: str) -> 'CORSConfig':
        """Configuración para frontend"""
        origins = {f"https://{domain}", f"http://{domain}", "http://localhost:3000", "http://127.0.0.1:3000"}
        return cls(
            allow_origins=origins,
            allow_credentials=True
        )
    
    @classmethod
    def frontend_public_api(cls, domain: str) -> 'CORSConfig':
        """Configuración para API pública de frontend"""
        origins = {f"https://{domain}", f"http://{domain}", "http://localhost:3000", "http://127.0.0.1:3000"}
        return cls(
            allow_origins=origins,
            allow_methods=["GET", "POST", "OPTIONS"],
            allow_headers=["Content-Type", "Authorization", "X-Requested-With"],
            expose_headers=["Content-Type", "Content-Length"],
            allow_credentials=False
        )
    
    @classmethod
    def frontend_private_api(cls, domain: str) -> 'CORSConfig':
        """Configuración para API privada de frontend"""
        origins = {f"https://{domain}", f"http://{domain}", "http://localhost:3000", "http://127.0.0.1:3000"}
        return cls(
            allow_origins=origins,
            allow_credentials=True
        )
    
    @classmethod
    def frontend_subdomain(cls, domain: str, subdomains: List[str]) -> 'CORSConfig':
        """Configuración para subdominios de frontend"""
        origins = {"http://localhost:3000", "http://127.0.0.1:3000"}
        for subdomain in subdomains:
            origins.add(f"https://{subdomain}.{domain}")
            origins.add(f"http://{subdomain}.{domain}")
        
        return cls(
            allow_origins=origins,
            allow_credentials=True
        )
    
    @classmethod
    def frontend_subdomain_public_api(cls, domain: str, subdomains: List[str]) -> 'CORSConfig':
        """Configuración para API pública de subdominios de frontend"""
        origins = {"http://localhost:3000", "http://127.0.0.1:3000"}
        for subdomain in subdomains:
            origins.add(f"https://{subdomain}.{domain}")
            origins.add(f"http://{subdomain}.{domain}")
        
        return cls(
            allow_origins=origins,
            allow_methods=["GET", "POST", "OPTIONS"],
            allow_headers=["Content-Type", "Authorization", "X-Requested-With"],
            expose_headers=["Content-Type", "Content-Length"],
            allow_credentials=False
        )
    
    @classmethod
    def frontend_subdomain_private_api(cls, domain: str, subdomains: List[str]) -> 'CORSConfig':
        """Configuración para API privada de subdominios de frontend"""
        origins = {"http://localhost:3000", "http://127.0.0.1:3000"}
        for subdomain in subdomains:
            origins.add(f"https://{subdomain}.{domain}")
            origins.add(f"http://{subdomain}.{domain}")
        
        return cls(
            allow_origins=origins,
            allow_credentials=True
        )
    
    def as_dict(self) -> Dict[str, Any]:
        """Convertir la configuración a diccionario para FastAPI"""
        return {
            "allow_origins": list(self.allow_origins),
            "allow_methods": self.allow_methods,
            "allow_headers": self.allow_headers,
            "expose_headers": self.expose_headers,
            "allow_credentials": self.allow_credentials,
            "max_age": self.max_age
        }