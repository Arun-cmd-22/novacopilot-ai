from sqlalchemy import Column, ForeignKey, Integer
from sqlalchemy.orm import relationship

from app.database.database import Base


class RolePermission(Base):
    __tablename__ = "role_permissions"

    id = Column(
        Integer,
        primary_key=True,
        autoincrement=True
    )

    role_id = Column(
        Integer,
        ForeignKey("roles.id", ondelete="CASCADE"),
        nullable=False
    )

    permission_id = Column(
        Integer,
        ForeignKey("permissions.id", ondelete="CASCADE"),
        nullable=False
    )

    role = relationship("Role")

    permission = relationship("Permission")