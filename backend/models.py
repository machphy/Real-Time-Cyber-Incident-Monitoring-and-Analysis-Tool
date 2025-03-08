from sqlalchemy import Column, Integer, String, DateTime
from database import Base
import datetime

class Incident(Base):
    __tablename__ = "incidents"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, index=True)
    description = Column(String)
    timestamp = Column(DateTime, default=datetime.datetime.utcnow)
