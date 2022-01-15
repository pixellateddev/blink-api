from fastapi import FastAPI

from .settings import settings
from .events import startup, shutdown

from users.router import router as users_router


app = FastAPI(debug=settings.DEBUG)

app.add_event_handler('startup', startup)
app.add_event_handler('shutdown', shutdown)

app.include_router(users_router, tags=['users'], prefix='/users')