from datetime import datetime
from typing import List

from pydantic import BaseModel


class Patient(BaseModel):
    id: int
    date_of_birth: datetime
    diagnoses: List[str]
    created_at: datetime
