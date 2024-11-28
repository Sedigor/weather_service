from fastapi import APIRouter, Query
from app.services.weather import get_weather

router = APIRouter()

@router.get("/")
async def fetch_weather(city: str = Query(..., description="Назва міста")):
    """
    Отримати поточну погоду для заданого міста.
    """
    weather_data = await get_weather(city)
    return weather_data
