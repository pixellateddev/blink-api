from fastapi import FastAPI

from .settings import settings
from .events import startup, shutdown

from users.router import router as users_router
from auth.router import router as auth_router


app = FastAPI(debug=settings.DEBUG)

app.add_event_handler('startup', startup)
app.add_event_handler('shutdown', shutdown)

app.include_router(users_router, tags=['users'], prefix='/users')
app.include_router(auth_router, tags=['auth'], prefix='/auth')