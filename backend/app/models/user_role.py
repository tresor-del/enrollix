from sqlalchemy import UUID, Column, Integer, ForeignKey
from sqlalchemy.orm import relationship
from app.db.database import Base
class UserRole(Base):
    __tablename__ = "user_roles"

    user_id = Column(UUID(as_uuid=True), ForeignKey("users.id"), primary_key=True)
    role_id = Column(UUID(as_uuid=True), ForeignKey("roles.id"), primary_key=True)

    # relations optionnelles si tu veux
    user = relationship("User")
    role = relationship("Role")
