from sqlalchemy import create_engine, select, String, Integer, Float
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, Session
from sqlalchemy.exc import SQLAlchemyError


# Conexión con SQLite. El archivo se crea automáticamente si no existe.
engine = create_engine("sqlite:///zapateria.db", echo=False)


# Clase base para los modelos ORM.
class Base(DeclarativeBase):
    pass


# Modelo que representa la tabla "zapatos".
class Zapato(Base):
    __tablename__ = "zapatos"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    modelo: Mapped[str] = mapped_column(String(100), nullable=False)
    talla: Mapped[int] = mapped_column(Integer, nullable=False)
    precio: Mapped[float] = mapped_column(Float, nullable=False)

    def __repr__(self):
        return (
            f"Zapato(id={self.id}, modelo={self.modelo!r}, "
            f"talla={self.talla}, precio={self.precio})"
        )


def inicializar_bd():
    """Crea la tabla definida en los modelos si todavía no existe."""
    Base.metadata.create_all(engine)


def crear_zapato(modelo, talla, precio):
    """Registra un zapato. Devuelve True si se guardó correctamente."""
    try:
        with Session(engine) as sesion:
            zapato = Zapato(modelo=modelo, talla=talla, precio=precio)
            sesion.add(zapato)
            sesion.commit()
            return True
    except SQLAlchemyError:
        return False


def listar_zapatos():
    """Devuelve una lista con todos los zapatos registrados."""
    with Session(engine) as sesion:
        consulta = select(Zapato).order_by(Zapato.id)
        return list(sesion.scalars(consulta).all())


def buscar_zapato(id_zapato):
    """Devuelve el zapato con ese ID o None cuando no existe."""
    with Session(engine) as sesion:
        return sesion.get(Zapato, id_zapato)


def actualizar_precio(id_zapato, nuevo_precio):
    """Actualiza el precio. Devuelve False si el ID no existe."""
    try:
        with Session(engine) as sesion:
            zapato = sesion.get(Zapato, id_zapato)
            if zapato is None:
                return False

            zapato.precio = nuevo_precio
            sesion.commit()
            return True
    except SQLAlchemyError:
        return False


def eliminar_zapato(id_zapato):
    """Elimina el zapato indicado. Devuelve False si no existe."""
    try:
        with Session(engine) as sesion:
            zapato = sesion.get(Zapato, id_zapato)
            if zapato is None:
                return False

            sesion.delete(zapato)
            sesion.commit()
            return True
    except SQLAlchemyError:
        return False
