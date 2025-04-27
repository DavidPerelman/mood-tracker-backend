# main.py

from fastapi import FastAPI
from api.mood import router as mood_router
from api.emotions import router as emotions_router

app = FastAPI()

# חיבור ה-endpoints
app.include_router(mood_router)
app.include_router(emotions_router)
