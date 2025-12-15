import bcrypt
import jwt
from fastapi import APIRouter, Depends, HTTPException, status
from schemas.users import UserSchema
from dependencies import connect_db
from sqlalchemy.orm import Session
from models.users import Users
from schemas.users import UserSchema
from schemas.signin import SignInSchema
from dependencies import connect_db


users_router = APIRouter(prefix="/users", tags=["users"])


@users_router.post("/signin")
async def signin_user(credentials: SignInSchema, dbs: Session = Depends(connect_db)):
    try:
        # find the email id is valid or not
        is_valid_email = (
            dbs.query(Users).filter(Users.email == credentials.email).first()
        )
        if not is_valid_email:
            return {"message": "incorrect email address"}
        else:
            # find the hashed portion of the pass word and compare it with the database
            plain_password_bytes = credentials.password.encode()
            hashed_password_bytes = is_valid_email.password.encode()
            if not bcrypt.checkpw(plain_password_bytes, hashed_password_bytes):
                return {"message": "invalid password"}
            return {"message": "sign in success"}
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="unexpected error has happened",
        )
