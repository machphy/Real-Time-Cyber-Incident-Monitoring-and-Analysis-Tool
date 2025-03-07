from database import Base, engine

# Yeh command sare table crete krea .
Base.metadata.create_all(bind=engine)
