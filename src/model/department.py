from src.database.base import Base
from sqlalchemy import column

class Department_class(Base):
    __tablename__="Department"

    department_id = column(...,nullable=False)
    department_name = column(...,nullable=False)
    department_description = column(...,nullable=False)
