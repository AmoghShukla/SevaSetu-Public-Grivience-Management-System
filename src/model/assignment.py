from src.database.base import Base
from sqlalchemy import column, Integer, String, ForeignKey, Text, DateTime
from sqlalchemy.orm import relationship

class Assignment_Class(Base):
    __tablename__="Assignment"

    assignment_id = column(Integer, primary_key=True, index=True)
    grivience_id = column(Integer, ForeignKey('Grivience.grivience_id'), nullable=False)
    officer_id = column(Integer, ForeignKey('User.user_id'), nullable=False)
    assigned_by = column(Integer, ForeignKey('User.uder_id'), nullable=False)
    assigned_at = column(DateTime, default = DateTime.now)
    current_status = 

