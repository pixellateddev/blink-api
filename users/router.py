from fastapi_utils.cbv import cbv
from fastapi_utils.inferring_router import InferringRouter

from .models import User

router = InferringRouter()


@cbv(router)
class UserViewSet:

    @router.get('/')
    async def list_users(self):
        users = await User.find_all()
        return users
