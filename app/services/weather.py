import os
import httpx
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv("OPENWEATHER_API_KEY")
BASE_URL = "http://api.openweathermap.org/data/2.5/weather"

async def get_weather(city: str):
    """
    Отримуємо погоду для заданого міста.
    """
    params = {
        "q": city,
        "appid": API_KEY,
        "units": "metric",  # Для відображення температури в градусах Цельсія
        "lang": "uk",       # Для української мови
    }

    async with httpx.AsyncClient() as client:
        response = await client.get(BASE_URL, params=params)
        if response.status_code == 200:
            return response.json()
        else:
            return {"error": f"Unable to fetch weather: {response.text}"}
