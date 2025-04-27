# db/mongodb.py

from pymongo import MongoClient

client = MongoClient("mongodb://localhost:27017")
db = client["mood_tracker"]  # שם מסד הנתונים
collection = db["mood_entries"]  # שם האוסף (collection)
