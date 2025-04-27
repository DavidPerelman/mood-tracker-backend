# models.py

from pydantic import BaseModel
from typing import Optional

class MoodEntry(BaseModel):
    mood_score: int  # מצב רוח בסולם 1-10
    emotions: list[str]  # רשימת רגשות שהמשתמש מרגיש
    reasons: Optional[list[str]] = None  # סיבות אפשריות למצב רוח (לא חובה)
    notes: Optional[str] = None  # הערות אישיות

    class Config:
        min_anystr_length = 1
        anystr_strip_whitespace = True
