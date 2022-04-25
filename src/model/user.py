from src.service.mongo import Mongo
from bson.objectid import ObjectId
from src.model.dto.userDto import UserDtoGetById

db = Mongo().mongo_connect()


class UserModel:

    list_fields = [
        "user_id",
        "name",
        "email",
        "login",
        "password",
        "activated",
        "age",
        "description",
        "city",
    ]

    def get_all(self):
        db_result = list(db.users.find())
        if not db_result:
            return None

        payload_users = []
        for user in db_result:
            payload_users.append(UserDtoGetById(**user).dict())

        return payload_users

    def get_by_id(self, id):
        db_result = db.users.find_one({"_id": ObjectId(id)})
        if not db_result:
            return None
        data_result = UserDtoGetById(**db_result)

        return data_result

    def add(self, payload):
        new_user = payload.dict()
        db_result = db.users.insert_one(new_user)
        if not db_result:
            return None

        return db_result

    def update(self, id, payload):
        user_update = payload.dict()
        db_result = db.users.update_one(
            {"_id": ObjectId(id)},
            {"$set": user_update},
        )
        if not db_result:
            return None
        return db_result

    def delete(self, id):
        db_result = db.users.delete_one({"_id": ObjectId(id)})
        return db_result
