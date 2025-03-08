from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.orm import sessionmaker, scoped_session, declarative_base

# Database Connection URL
DATABASE_URL = "postgresql://rajeev:123456789@localhost/cyber_incidents"

# Create Engine
engine = create_engine(DATABASE_URL)

# ✅ Session Banane Ka Tarika (Scoped Session)
SessionLocal = scoped_session(sessionmaker(autocommit=False, autoflush=False, bind=engine))

# ✅ Base Model
Base = declarative_base()

# ✅ Incident Model
class Incident(Base):
    __tablename__ = "incidents"

    id = Column(Integer, primary_key=True, index=True)
    description = Column(String, index=True)
    severity = Column(String)
    status = Column(String, default="open")

# ✅ Initialize Database
def init_db():
    Base.metadata.create_all(bind=engine)

# ✅ Export Session for Use
db_session = SessionLocal
