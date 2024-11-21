from server.external_interface import users_api_client


class UsersRepository:
    last_id: int = 0
    fake_db: list[dict] = []

    def create(self, new_user: dict) -> dict:
        from datetime import datetime
        now = datetime.now()
        UsersRepository.last_id += 1
        new_user.update(
            id=UsersRepository.last_id,
            created_at=now,
            updated_at=now,
        )
        UsersRepository.fake_db.append(new_user)
        return new_user

    def get_list(self, limit: int, offset: int) -> list[dict]:
        db_size = len(UsersRepository.fake_db)
        first_index = min(db_size, offset)
        last_index = min(db_size, (first_index + limit))
        return UsersRepository.fake_db[first_index:last_index]

    def get_by_id(self, id: int) -> dict | None:
        for user in UsersRepository.fake_db:
            if user['id'] == id:
                return user

    def update(self, id: int, new_data: dict) -> dict | None:
        from datetime import datetime
        now = datetime.now()
        current_user = self.get_by_id(id)
        if current_user is None:
            return None
        current_user.update(**new_data, updated_at=now)
        return current_user

    def delete(self, id: int) -> bool:
        current_user = self.get_by_id(id)
        if current_user is None:
            return False
        UsersRepository.fake_db.remove(current_user)
        return True
