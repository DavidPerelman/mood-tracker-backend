# api/mood.py

from fastapi import APIRouter
from models.mood_entry import MoodEntry
from db.mongodb import collection

router = APIRouter()

@router.post("/mood")
def create_mood_entry(mood_entry: MoodEntry):
    # המרת הרשומות למילון (dictionary) עבור MongoDB
    mood_entry_dict = mood_entry.dict()
    mood_entry_dict["emotions"] = ", ".join(mood_entry.emotions)
    mood_entry_dict["reasons"] = ", ".join(mood_entry.reasons) if mood_entry.reasons else None
    
    # הוספת הרשומה ל-MongoDB
    result = collection.insert_one(mood_entry_dict)
    
    return {"message": "Mood entry created!", "id": str(result.inserted_id)}
