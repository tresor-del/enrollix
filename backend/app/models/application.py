import uuid
from sqlalchemy import UUID, Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from app.db.database import Base

class Application(Base):
    __tablename__ = "applications"

    id = Column(UUID(as_uuid=True), primary_key=True, index=True, default=uuid.uuid4)
    student_id = Column(UUID(as_uuid=True), ForeignKey("users.id"))
    programme_id = Column(UUID(as_uuid=True), ForeignKey("programmes.id"))
    year_id = Column(UUID(as_uuid=True), ForeignKey("academic_years.id"))
    status = Column(String, default="draft")  # draft, submitted, validated, rejected

    student = relationship("User", back_populates="applications")
    programme = relationship("Programme", back_populates="applications")
    year = relationship("AcademicYear", back_populates="applications")
