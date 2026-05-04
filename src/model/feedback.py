from src.database.base import Base
from sqlalchemy import UUID, column

class Feedback_Class(Base):
    __tablename__="Feedback_Table"

    feedback_id = column(UUID, primary_key = True, index = True)

