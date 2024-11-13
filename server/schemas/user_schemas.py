from datetime import datetime

from pydantic import BaseModel, Field, EmailStr


class NewUserRequest(BaseModel):
    legajo: int = Field(..., ge=1, description="Número de legajo del usuario, debe ser positivo")
    nombre: str
    apellido: str
    telefono: str
    email: EmailStr


class UserRequest(BaseModel):
    legajo: int | None = Field(None, ge=1, description="Número de legajo del usuario, debe ser positivo")
    nombre: str | None = None
    apellido: str | None = None
    telefono: str | None = None
    email: EmailStr | None = None


class UserResponse(BaseModel):
    id: int
    legajo: int
    nombre: str
    apellido: str
    telefono: str
    email: EmailStr
    created_at: datetime
    updated_at: datetime
