from fastapi import APIRouter, Depends
from sqlalchemy import select

from app.db.models import Patient
from app.db.sqlalchemy import session_fabric
from app.dependencies.dependency import check_token
from app.schemas.patient import PatientSchema
from app.schemas.token import TokenData

router = APIRouter()


# Adapter for getting patients
@router.get("/")
async def get_patients(token_data: TokenData = Depends(check_token)):
    async with session_fabric.get_session() as session, session.begin():
        query = select(Patient)
        rows = await session.execute(query)
        patients_db = rows.scalars().unique().all()

    return [PatientSchema.from_orm(patient) for patient in patients_db]
