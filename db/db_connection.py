from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

#Creando Motor y Conexión con la base de datos
DATABASE_URL = "postgresql://postgres:2420112006@localhost:5432/MISIONTIC"
engine = create_engine(DATABASE_URL)

#Creación de la sesión
SessionLocal = sessionmaker(autocommit=False,
                            autoflush=False,
                            bind=engine)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

#Creando base para la creación de los modelos
Base = declarative_base()
Base.metadata.schema = "cajerodb"