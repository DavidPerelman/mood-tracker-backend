# models/mood_entry.py

from pydantic import BaseModel, validator
from typing import List

# רשימה קבועה של רגשות אפשריים
AVAILABLE_EMOTIONS = [
    "Happy", "Sad", "Angry", "Anxious", "Excited", "Bored", "Calm", "Stressed", "Confused", "Grateful"
]

class MoodEntry(BaseModel):
    mood_score: int
    emotions: List[str]
    reasons: List[str] = None
    notes: str = None

    # מאמת שהרגשות הנבחרים הם מתוך הרשימה הקבועה
    @validator('emotions')
    def check_emotions_validity(cls, v):
        for emotion in v:
            if emotion not in AVAILABLE_EMOTIONS:
                raise ValueError(f"Emotion '{emotion}' is not a valid choice. Choose from {AVAILABLE_EMOTIONS}.")
        return v
