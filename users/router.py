from typing import List
from pydantic.error_wrappers import ValidationError
from fastapi import status, HTTPException, Response, Depends
from fastapi_utils.cbv import cbv
from fastapi_utils.inferring_router import InferringRouter

from users.schema import UserSchema
from auth.auth import get_current_user

from .models import User

router = InferringRouter()


@cbv(router)
class UserViewSet:

    user: User = Depends(get_current_user)

    @router.get('/')
    async def list_users(self) -> List[UserSchema]:
        users = await User.find_all()
        return users

    
    @router.get('/me')
    async def me(self) -> UserSchema:
        '''Returns the current logged in user'''
        return self.user.dump()
    
