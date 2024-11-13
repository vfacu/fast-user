from fastapi import FastAPI

from .api import api_router


fast_users = FastAPI()

# Incluimos el router principal a la instancia de FastAPI
fast_users.include_router(api_router)