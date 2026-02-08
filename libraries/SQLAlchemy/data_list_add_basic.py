from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.orm import declarative_base, sessionmaker

# 1. Crear conexión a SQLite (archivo local)
engine = create_engine("sqlite:///libraries/SQLAlchemy/ejemplo.db", echo=True)

# 2. Base para modelos
Base = declarative_base()

# 3. Definir tabla (modelo)
class Usuario(Base):
    __tablename__ = "usuarios"

    id = Column(Integer, primary_key=True)
    nombre = Column(String)
    email = Column(String)

# 4. Crear la tabla en la BD
Base.metadata.create_all(engine)

# 5. Crear sesión
Session = sessionmaker(bind=engine)
session = Session()

# 6. INSERT
usuario1 = Usuario(nombre="Juan", email="juan@mail.com")
session.add(usuario1)
session.commit()

# 7. SELECT
usuarios = session.query(Usuario).all()

print("Usuarios en la BD:")
for u in usuarios:
    print(u.id, u.nombre, u.email)
