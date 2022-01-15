import uvicorn
from blink.settings import settings


if __name__ == '__main__':
    uvicorn.run(
        'blink.app:app',
        host=settings.HOST,
        port=settings.PORT,
        reload=settings.DEBUG
    )