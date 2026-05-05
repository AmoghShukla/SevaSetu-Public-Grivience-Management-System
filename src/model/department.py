from uuid import UUID, uuid4

from src.database.base import Base
from sqlalchemy import column

class Department_class(Base):
    __tablename__="Department"

    department_id = column(UUID(as_UUID=True), default=uuid4,nullable=False)
    department_name = column(...,nullable=False)
    department_description = column(...,nullable=False)
