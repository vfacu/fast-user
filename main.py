import uvicorn

from server.configs import app_settings as settings

if __name__ == '__main__':
    uvicorn.run('server.app:fast_users', host='0.0.0.0',
                port=settings.PORT, reload=settings.DEV)
