from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

DATABASE_URL = "mysql+mysqlconnector://root:123456@localhost:3306/PPAI"

# DATABASE_URL = "mysql+mysqlconnector://root:~~TU CONTRASEÑA de sql~~@localhost:3306/PPAI"

engine = create_engine(DATABASE_URL, echo=False)
SessionLocal = sessionmaker(bind=engine)
Base = declarative_base()
