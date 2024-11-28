from fastapi import FastAPI
from app.routes import weather

app = FastAPI(
    title="Weather Service",
    description="API для отримання даних про погоду",
    version="1.0.0"
)

# Підключаємо маршрути
app.include_router(weather.router, prefix="/weather", tags=["Weather"])

@app.get("/")
def root():
    return {"message": "Welcome to the Weather Service API"}


import os
from dotenv import load_dotenv

load_dotenv()

OPENWEATHER_API_KEY = os.getenv("OPENWEATHER_API_KEY")
print(f"Your API Key: {OPENWEATHER_API_KEY}")  # Перевірка, чи ключ завантажено
