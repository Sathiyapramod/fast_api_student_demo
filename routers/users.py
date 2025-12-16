import bcrypt
import jwt
from fastapi import APIRouter, Depends, HTTPException, status
from dependencies import connect_db
from sqlalchemy.orm import Session
from models.users import Users
from schemas.users import RegisterUser
from schemas.signin import SignInSchema
from dependencies import connect_db
from core.jwt import create_access_token
from core.bcrypt import hashing_password, verify_password


users_router = APIRouter(prefix="/users", tags=["users"])


@users_router.post("/signin", status_code=status.HTTP_200_OK)
def signin_user(credentials: SignInSchema, dbs: Session = Depends(connect_db)):
    # find the email id is valid or not
    user = dbs.query(Users).filter(Users.email == credentials.email).first()

    if not user or not verify_password(
        credentials.password.encode(), user.password.encode()
    ):
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST, detail="Invalid email or password"
        )

    new_token = create_access_token({"username": user.username, "email": user.email})

    return {
        "message": "Sign in successful",
        "token_type": "bearer",
        "user_id": user.id,
        "token": new_token,
    }


@users_router.post("/signup", status_code=status.HTTP_200_OK)
def register_user(credentials: RegisterUser, dbs: Session = Depends(connect_db)):
    existing_user = dbs.query(Users).filter(Users.email == credentials.email).first()
    if existing_user:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST, detail="Email Already exists"
        )

    hashed_password = hashing_password(credentials.password)

    new_user = Users(
        email=credentials.email, username=credentials.username, password=hashed_password
    )

    dbs.add(new_user)
    dbs.commit()
    dbs.refresh(new_user)
    return {"message": "new user created"}
