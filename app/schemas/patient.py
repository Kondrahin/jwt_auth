from datetime import datetime
from typing import List

from pydantic import BaseModel

from app.db.models import Patient


class PatientSchema(BaseModel):
    id: int
    date_of_birth: datetime
    diagnoses: List[str]
    created_at: datetime

    @classmethod
    def from_orm(cls, patient: Patient) -> "PatientSchema":
        diagnoses = [diagnose.diagnose_name for diagnose in patient.diagnoses]
        return cls(
            id=patient.id,
            date_of_birth=patient.date_of_birth,
            diagnoses=diagnoses,
            created_at=patient.created_at
        )
