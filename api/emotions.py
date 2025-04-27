# api/emotions.py

from fastapi import APIRouter

router = APIRouter()

# רשימה קבועה של רגשות
AVAILABLE_EMOTIONS = [
    "Happy", "Sad", "Angry", "Anxious", "Excited", "Bored", "Calm", "Stressed", "Confused", "Grateful"
]

@router.get("/emotions")
def get_emotions():
    return {"emotions": AVAILABLE_EMOTIONS}
