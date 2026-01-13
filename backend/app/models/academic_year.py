import uuid
from sqlalchemy import Column, Integer, Boolean
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import relationship
from app.db.database import Base

class AcademicYear(Base):
    __tablename__ = "academic_years"

    id = Column(UUID(as_uuid=True), primary_key=True, index=True, default=uuid.uuid4)
    start_year = Column(Integer, nullable=False)
    end_year = Column(Integer, nullable=False)
    active = Column(Boolean, default=False)

    applications = relationship("Application", back_populates="year")
