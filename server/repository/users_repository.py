# from server.external_interface import users_api_client
from server.database import db_connection
from server.database.models import UserModel


class UsersRepository:
    # last_id: int = 0
    # fake_db: list[dict] = []
    def __init__(self):
        self.db = db_connection.session

    def create(self, new_user_dict: dict) -> dict:
        #    from datetime import datetime
        #    now = datetime.now()
        #    UsersRepository.last_id += 1
        #    new_user.update(
        #        id=UsersRepository.last_id,
        #        created_at=now,
        #        updated_at=now,
        #    )
        #    UsersRepository.fake_db.append(new_user)
        #    return new_user
        new_user = UserModel(**new_user_dict)
        self.db.add(new_user)
        self.db.commit()
        self.db.refresh(new_user)
        return self.__to_dict(new_user)

    def get_list(self, limit: int, offset: int) -> list[dict]:
        # db_size = len(UsersRepository.fake_db)
        # first_index = min(db_size, offset)
        # last_index = min(db_size, (first_index + limit))
        # return UsersRepository.fake_db[first_index:last_index]
        users = self.db.query(UserModel).order_by(
            'id').limit(limit).offset(offset).all()
        return [self.__to_dict(users) for users in users]

    def get_by_id(self, user_id: int) -> dict | None:
        # for user in UsersRepository.fake_db:
        #    if user['id'] == id:
        #        return user
        user = self.__get_one(user_id)
        if user is None:
            return
        return self.__to_dict(user)

    def update(self, id: int, new_data: dict) -> dict | None:
        # from datetime import datetime
        # now = datetime.now()
        # current_user = self.get_by_id(id)
        # if current_user is None:
        #    return None
        # current_user.update(**new_data, updated_at=now)
        # return current_user
        user = self.__get_one(id)
        if user is None:
            return
        for field in new_data.keys():
            setattr(user, field, new_data[field])
        self.db.commit()
        self.db.refresh(user)
        return self.__to_dict(user)

    def delete(self, id: int) -> bool:
        # current_user = self.get_by_id(id)
        # if current_user is None:
        #    return False
        # UsersRepository.fake_db.remove(current_user)
        # return True
        user = self.__get_one(id)
        if user is None:
            return False
        self.db.delete(user)
        self.db.commit()
        return True

    def __get_one(self, user_id: int) -> UserModel | None:
        return self.db.query(UserModel).filter_by(id=user_id).first()

    def __to_dict(self, user: UserModel) -> dict:
        return {
            column.name: getattr(user, column.name)
            for column in UserModel.__table__.columns
        }
