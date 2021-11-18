from fastapi import HTTPException, Depends
from fastapi.security import OAuth2PasswordBearer
from jose import jwt, JWTError
from pydantic import ValidationError
from starlette import status

from app.schemas.token import TokenData
from app.settings.config import config

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")


# Dependency for checking token
async def check_token(token: str = Depends(oauth2_scheme)):
    authenticate_value = f"Bearer"
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Could not validate credentials",
        headers={"WWW-Authenticate": authenticate_value},
    )
    not_doctor_exception = HTTPException(
        status_code=status.HTTP_403_FORBIDDEN,
        detail="You are not a doctor",
        headers={"WWW-Authenticate": authenticate_value},
    )
    try:
        payload = jwt.decode(token, config.SECRET_KEY, algorithms=[config.ALGORITHM])
        is_doctor = payload.get("isDoctor")
        if is_doctor is None:
            raise credentials_exception
        if is_doctor is False:
            raise not_doctor_exception
        token_data = TokenData(is_doctor=is_doctor)
    except (JWTError, ValidationError):
        raise credentials_exception

    return token_data
