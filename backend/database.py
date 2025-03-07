from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm import declarative_base


DATABASE_URL = "postgresql://rajeev:123456789@localhost/cyber_incidents"

engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()

class Incident(Base):
    __tablename__ = "incidents"

    id = Column(Integer, primary_key=True, index=True)
    description = Column(String, index=True)
    severity = Column(String)
    status = Column(String, default="open")

# ✅ Table Create Karne Ke Liye
Base.metadata.create_all(bind=engine)
