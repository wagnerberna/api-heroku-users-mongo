from src.model.dto import loginDto
from src.service.mongo import Mongo
from bson.objectid import ObjectId
from src.model.dto.loginDto import LoginDto

db = Mongo().mongo_connect()


class LoginModel:

    def find_login(self, login):
        find_login_db = db.users.find_one({"login": login})
        if not find_login_db:
            return None
        
        data_result=LoginDto(**find_login_db)
        return data_result

    def update_status(self, login, status):
        data = db.users.update_one({"login": login}, {"$set": {"activated": status}})

        if not data:
            return None
        return data
