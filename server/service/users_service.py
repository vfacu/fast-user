from typing import List
from server.schemas.user_schemas import NewUserRequest, UserResponse, UserRequest
from server.exceptions import NotFound


class UsersService:
    last_id: int = 0
    fake_db: list[dict] = []

    def __init__(self):
        # TODO: instanciar repo
        pass

    def create(self, new_user: NewUserRequest) -> UserResponse:
        # TODO:
        #! 1. Recibir el objeto de tipo NewUserResponse, convertirlo a diccionario, y pasarlo a la capa de repositorio
        #! 2. Recibimos del repo la respuesta (probablemente un diccionario o un objeto), lo convertimos a UserResponse y lo retornamos
        user_dict = self.__fake_create(new_user.model_dump())
        return UserResponse(**user_dict)

    def get_list(self, limit: int, offset: int) -> List[UserResponse]:
        # TODO:
        #! 1. Recibir los parámetros limit y offset y pasarlos a la capa repo
        #! 2. Recibir la lista de diccionarios u objetos, convertirlos a una lista de UserResponse y retornarlo
        user_list = self.__fake_get_list(limit, offset)
        return [UserResponse(**user) for user in user_list]

    def get_by_id(self, id: int) -> UserResponse:
        # TODO:
        #! 1. Recibimos el id de los parámetros y pasamos al repo
        #! 2. Recibimos el objeto o diccionario del repo, lo convertimos a un UserResponse y lo retornamos
        user = self.__fake_get_by_id(id)
        if user is None:
            raise NotFound(f'Usuario con id #{id} no encontrado')
        return UserResponse(**user)

    def update(self, id: int, new_data: UserRequest) -> UserResponse:
        # TODO:
        #! 1. Recibimos los parámetros, convertimos el new_data a un diccionario y lo pasamos al repo
        #! 2. Recibimos el objeto o dict actualizado del repo, lo convertimos a UserResponse y lo retornamos
        updated_user = self.__fake_update(
            id, new_data.model_dump(exclude_none=True))
        if updated_user is None:
            raise NotFound(
                f'Usuario con id #{id} no encontrado para actualizarse')
        return UserResponse(**updated_user)

    def delete(self, id: int) -> None:
        # TODO:
        #! 1. Pasamos el id al repo y retornamos
        if not self.__fake_delete(id):
            raise NotFound(
                f'Usuario con id #{id} no encontrado para eliminarse')

    # ? FAKE METHODS
    def __fake_create(self, new_user: dict) -> dict:
        from datetime import datetime
        now = datetime.now()
        UsersService.last_id += 1
        new_user.update(
            id=UsersService.last_id,
            created_at=now,
            updated_at=now,
        )
        UsersService.fake_db.append(new_user)
        return new_user

    def __fake_get_list(self, limit: int, offset: int) -> list[dict]:
        db_size = len(UsersService.fake_db)
        first_index = min(db_size, offset)
        last_index = min((db_size - first_index), limit)
        return UsersService.fake_db[first_index:last_index]

    def __fake_get_by_id(self, id: int) -> dict | None:
        for user in UsersService.fake_db:
            if user['id'] == id:
                return user

    def __fake_update(self, id: int, new_data: dict) -> dict | None:
        from datetime import datetime
        now = datetime.now()
        current_user = self.__fake_get_by_id(id)
        if current_user is None:
            return None
        current_user.update(**new_data, updated_at=now)
        return current_user

    def __fake_delete(self, id: int) -> bool:
        current_user = self.__fake_get_by_id(id)
        if current_user is None:
            return False
        UsersService.fake_db.remove(current_user)
        return True
