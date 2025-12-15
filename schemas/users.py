from pydantic import BaseModel


class UserSchema(BaseModel):
    email_id: str
    password: str
    username: str
