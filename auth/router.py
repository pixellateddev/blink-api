from fastapi_utils.inferring_router import InferringRouter
from fastapi_utils.cbv import cbv
from fastapi import HTTPException, status, Response
from pydantic.error_wrappers import ValidationError


from users.schema import UserSchema, UserInDBSchema
from .schema import LoginBody
from users.models import User
from .auth import create_access_token


router = InferringRouter()

@cbv(router)
class Auth:
    @router.post('/login')
    async def login(self, body: LoginBody, response: Response):
        user = await User.authenticate_user(body.username, body.password)
        if not user:
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Incorrect username or password",
            )
        access_token = create_access_token(data={"sub": user.username})
        response.set_cookie(
            key="access_token", value=f"Bearer {access_token}", httponly=True
        )
        return {"status": "Successfully Logged In"}

    @router.post('/logout')
    async def logout(self, response: Response):
        response.delete_cookie(key="access_token")
        return {"status": "Successfully Logged Out"}


    @router.post('/create')
    async def create_user(self, user: UserInDBSchema) -> UserSchema:
        try:
            new_user = User(
                firstName=user.firstName, 
                lastName=user.lastName, 
                email=user.email, 
                username=user.username
            )
            new_user.set_password(user.password)
            await new_user.commit()

            return new_user.dump()

        except ValidationError:
            raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=f'username or email already exist')    


