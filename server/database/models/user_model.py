from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy import String, Integer
from pydantic import EmailStr

from .base_model import BaseModel


class UserModel(BaseModel):
    __tablename__ = 'users'

    legajo: Mapped[int] = mapped_column(Integer, nullable=False)
    dni: Mapped[str] = mapped_column(String(20), nullable=False)
    nombre: Mapped[str] = mapped_column(String(50), nullable=False)
    apellido: Mapped[str] = mapped_column(String(50), nullable=False)
    telefono: Mapped[str] = mapped_column(String(15), nullable=False)
    email: Mapped[EmailStr] = mapped_column(String(100), nullable=False)
