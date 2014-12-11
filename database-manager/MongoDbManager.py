__author__ = 'j'
from pymongo import MongoClient
class MongoDbManager:
    db_url = "mongodb://localhost:27017/"
    db_username = ""
    db_password = ""
    def __init__(self):
        pass
    def openDb(self):
        client = MongoClient(self.db_url)
        return client


