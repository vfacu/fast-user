from typing import Annotated, List

from fastapi import APIRouter, Query, Path

from server.schemas.user_schemas import NewUserRequest, UserRequest, UserResponse
from server.controller import UsersController
from server.exceptions import InternalServerError, NotFound

router = APIRouter(prefix='/users')
router.responses = {
    500: InternalServerError.as_dict(),
}
controller = UsersController()

@router.post(
    '',
    status_code=201,
    responses={
        201: {'description': 'Proyecto creado'},
    },
    description='Crea un proyecto nuevo con los campos pasados por Body Param. Falla si faltan alguno de los campos obligatorios.'
)  # POST /projects
async def create(new_user: NewUserRequest) -> UserResponse:
    # recibir un objeto
    return controller.create(new_user)

@router.get(
    '',
    status_code=200,
    responses={
        200: {'description': 'Listado de proyectos'},
    },
    description='Retorna una lista paginada con los proyectos del usuario. Si no hay proyectos para mostrar, retorna lista vacía.'
)  # GET /projects
async def get_list(limit: Annotated[int, Query(ge=1, le=1000)] = 10, offset: Annotated[int, Query(ge=0)] = 0) -> List[UserResponse]:
    print(f'Paginado limite {limit} y offset {offset}')
    return controller.get_list(limit, offset)

@router.get(
    '/{id}',
    status_code=200,
    responses={
        200: {'description': 'Proyecto encontrado'},
        404: NotFound.as_dict(),
        422: {'description': 'ID no es un entero válido'},
    },
    description='Retorna un proyecto por ID. Falla si el ID no existe.'
)  # GET /projects/{id}
async def get_by_id(id: Annotated[int, Path(ge=1)]) -> UserResponse:
    return controller.get_by_id(id)


@router.patch(
    '/{id}',
    status_code=200,
    responses={
        200: {'description': 'Proyecto actualizado'},
        404: NotFound.as_dict(),
        422: {'description': 'ID no es un entero válido'},
    },
    description='Actualiza un proyecto con la data del Body Param. Falla si el ID no existe.'
)  # PATCH /projects/{id}
async def update(id: Annotated[int, Path(ge=1)], user: UserRequest) -> UserResponse:
    return controller.update(id, user)


@router.delete(
    '/{id}',
    status_code=204,
    responses={
        204: {'description': 'Proyecto eliminado'},
        404: NotFound.as_dict(),
        422: {'description': 'ID no es un entero válido'},
    },
    description='Elimina un proyecto con id pasado por Path Param. Falla si el ID no existe.'
)  # DELETE /projects/{id}
async def delete(id: Annotated[int, Path(ge=1)]) -> None:
    controller.delete(id)
