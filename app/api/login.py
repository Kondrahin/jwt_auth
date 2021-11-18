from datetime import timedelta, datetime
from typing import Optional

from fastapi import APIRouter
from jose import jwt
from passlib.context import CryptContext
from app.schemas.token import Token
from app.settings.config import config

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

router = APIRouter()


# Function for generating access token
def create_access_token(data: dict, expires_delta: Optional[timedelta] = None):
    to_encode = data.copy()
    if expires_delta:
        expire = datetime.utcnow() + expires_delta
    else:
        expire = datetime.utcnow() + timedelta(minutes=15)
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(to_encode, config.SECRET_KEY, algorithm=config.ALGORITHM)
    return encoded_jwt


# Adapter for getting token
@router.get("/token", response_model=Token)
async def get_token():
    access_token_expires = timedelta(minutes=config.ACCESS_TOKEN_EXPIRE_MINUTES)
    access_token = create_access_token(
        data={"isDoctor": True},
        expires_delta=access_token_expires,
    )
    return {"access_token": access_token, "token_type": "bearer"}


