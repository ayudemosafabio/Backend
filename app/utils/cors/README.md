```python
app = FastAPI()
    
setup_cors(app, CORSType.CORS)

setup_cors(app, CORSType.PRIVATE_API, origins=["https://mi-dominio.com"])

setup_cors(app, CORSType.FRONTEND, domain="mi-dominio.com")

setup_cors(app, CORSType.FRONTEND_SUBDOMAIN, 
            domain="mi-dominio.com", 
            subdomains=["app", "dashboard", "admin"])
```