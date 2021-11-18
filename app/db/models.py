from datetime import datetime

import sqlalchemy as sa
from sqlalchemy.orm import relationship

from app.db.sqlalchemy import Base

association_table = sa.Table(
    "patient_diagnose_association",
    Base.metadata,
    sa.Column(
        "patient_id",
        sa.Integer,
        sa.ForeignKey("patient.id", ondelete="CASCADE"),
        primary_key=True,
    ),
    sa.Column(
        "diagnose_id",
        sa.Integer,
        sa.ForeignKey("diagnose.id", ondelete="CASCADE"),
        primary_key=True,
    ),
)


class Patient(Base):
    """Patient database model"""

    __tablename__ = "patient"

    id: int = sa.Column(sa.Integer, primary_key=True, autoincrement=True)  # noqa: WPS125
    date_of_birth: datetime = sa.Column(sa.DateTime, nullable=False)
    created_at: datetime = sa.Column(sa.DateTime, nullable=False)
    diagnoses = relationship(
        "Diagnose",
        secondary=association_table,
        back_populates="patients",
        lazy="joined",
        cascade="all,delete",
    )


class Diagnose(Base):
    """Diagnose database model."""

    __tablename__ = "diagnose"

    id: int = sa.Column(sa.Integer, primary_key=True, autoincrement=True)  # noqa: WPS125
    diagnose_name: str = sa.Column(sa.String, nullable=False)
    patients = relationship(
        "Patient",
        secondary=association_table,
        back_populates="diagnoses",
        lazy="joined",
        cascade="all,delete",
    )
