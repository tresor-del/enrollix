import uuid
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.dialects.postgresql import UUID
from app.db.database import Base

class Programme(Base):
    __tablename__ = "programmes"

    id = Column(UUID(as_uuid=True), primary_key=True, index=True, default=uuid.uuid4)
    name = Column(String, nullable=False)
    description = Column(String)
    domaine_id = Column(Integer, ForeignKey("domaines.id"))

    domaine = relationship("Domaines", back_populates="programmes")
    applications = relationship("Application", back_populates="programme")
