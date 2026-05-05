from uuid import UUID, uuid4

from src.database.base import Base
from sqlalchemy import column, Integer, String, ForeignKey, Text
from sqlalchemy.orm import relationship

class Grivience_Class(Base):
    __tablename__="Grivience"

    grivience_id = column(UUID(as_UUID=True), default=uuid4, primary_key=True, index=True)
    grivience_title = column(String, nullable=False)
    grivience_description = column(Text, nullable=False)

    user_id = column(Integer, ForeignKey("User"))
    grivience_status = column(...,nullable=False)
