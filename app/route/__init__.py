import importlib
import pkgutil
from fastapi import FastAPI, APIRouter

def include_package_routers(app: FastAPI, package):
    if isinstance(package, str):
        package = importlib.import_module(package)

    def _explore(pkg):
        for _, module_name, is_pkg in pkgutil.iter_modules(pkg.__path__):
            full_name = f"{pkg.__name__}.{module_name}"
            module = importlib.import_module(full_name)

            # Detectar routers en el módulo
            for attr_name in dir(module):
                attr = getattr(module, attr_name)
                if isinstance(attr, APIRouter):
                    app.include_router(attr)

            # Recurse subpackages
            if is_pkg:
                _explore(module)

    _explore(package)