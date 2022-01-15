from umongo import Document, fields

from blink.db import instance, BaseDocument
from utils.password import pass_utils


@instance.register
class User(Document, BaseDocument):
    username = fields.StringField(required=True, unique=True)
    email = fields.StringField(required=True, unique=True)
    firstName = fields.StringField(required=True)
    lastName = fields.StringField()
    password = fields.StringField(required=True)


    class Meta:
        collection_name = 'user'


    def __str__(self) -> str:
        return self.username
    
    def set_password(self, password:str) -> None:
        self.password = pass_utils.hash_password(password)

    def list_view(self):
        return {
            'username': self.username,
            'email': self.email,
            'firstName': self.firstName,
            'lastName': self.lastName
        }

    @classmethod
    async def authenticate_user(cls, username, password):
        user = await cls.find_one({
            'username': username,
        })

        if not user:
            return False
        
        if not pass_utils.verify_password(password, user.password):
            return False
        
        return user