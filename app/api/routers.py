
from fastapi import APIRouter

from app.api import login, patients

api_router = APIRouter()
api_router.include_router(login.router, tags=["login"])
api_router.include_router(patients.router, prefix="/patients", tags=["patients"])
