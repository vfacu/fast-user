import uvicorn


if __name__ == '__main__':
    uvicorn.run('server.app:fast_users', host='0.0.0.0', port=8000, reload=True)