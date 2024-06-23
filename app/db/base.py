from pymongo import MongoClient

from app.core.config import settings

MONGO_URL = settings.MONGO_URL
client = MongoClient(MONGO_URL)
MONGO_DB = settings.MONGO_DB

def get_database():
    return client[MONGO_DB]