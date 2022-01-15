from motor.motor_asyncio import AsyncIOMotorClient
from umongo.frameworks import MotorAsyncIOInstance
from .settings import settings

instance = MotorAsyncIOInstance()


def init_db():
    client = AsyncIOMotorClient(settings.DB_URI)
    db = client[settings.DB_NAME]
    instance.set_db(db=db)


class BaseDocument:
    @classmethod
    async def find_all(cls, query: dict = {}):
        items = []
        async for item in cls.find(query):
            items.append(item.list_view())

        return items

    
    def list_view(self):
        return self.dump()