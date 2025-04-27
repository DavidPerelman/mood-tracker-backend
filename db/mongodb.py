# db/mongodb.py

from pymongo import MongoClient

# התחברות ל-MongoDB
client = MongoClient("mongodb://localhost:27017")
db = client.mood_tracker
collection = db.mood_entries
emotions_collection = db.emotions


def get_db():
    return db
