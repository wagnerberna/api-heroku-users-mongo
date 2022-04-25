from src.static.message import ERROR_MESSAGE
from pymongo import MongoClient
import os
from dotenv import load_dotenv

load_dotenv()
MONGO_SERVER = os.getenv("MONGO_SERVER")
DATABASE=os.getenv("DATABASE")

class Mongo:
    def mongo_connect(self):
        try:
            client = MongoClient(MONGO_SERVER)
            db = client[DATABASE]
            client.server_info()
            return db
            
        except Exception as error:
            print(ERROR_MESSAGE.format(error))
            # print("ERROR - Cannot connect to db")
