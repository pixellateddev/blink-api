from .db import init_db

async def startup():
    print('startup')
    init_db()


async def shutdown():
    print('shutdown')