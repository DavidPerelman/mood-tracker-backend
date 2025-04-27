# main.py

from fastapi import FastAPI
from models import MoodEntry

app = FastAPI()

@app.get("/health")
def health_check():
    return {"status": "ok"}

# הוספת MoodEntry
@app.post("/mood")
def create_mood_entry(mood_entry: MoodEntry):
    return {"message": "Mood entry created!", "data": mood_entry}
