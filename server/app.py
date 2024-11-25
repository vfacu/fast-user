from fastapi import FastAPI

from .api import api_router
from .database import db_connection


fast_users = FastAPI()

fast_users.include_router(api_router)


@fast_users.on_event('startup')
async def startup_event():
    # if db_connection.connect():
    #    create_tables()
    db_connection.connect()


@fast_users.on_event('shutdown')
def shutdown_event():
    db_connection.disconnect
