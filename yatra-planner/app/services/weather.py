from datetime import date
import os

import httpx

from ..model import WeatherResponseModel
from .cache import get_cache, set_cache

async def fetch_weather_data(
    destination:str,
    start_date: date,
    end_date: date
) -> list[WeatherResponseModel]:
    cache_key = f"{destination}_{start_date}_{end_date}"
    cache_data = get_cache(cache_key)

    if cache_data:
        return cache_data # type: ignore

    api_key = os.getenv("WEATHER_API_KEY")
    if not api_key:
        raise RuntimeError("WEATHER_API_KEY environment variable is required")
    
    async with httpx.AsyncClient() as client:
        response = await client.get(
            f"https://api.weatherapi.com/v1/forecast.json",
            params={
                "key": api_key,
                "q": destination,
                "dt": start_date.isoformat(),
                "end_dt": end_date.isoformat()
            }
        )
        response.raise_for_status()
        data = response.json()

        forecasts = []

        for day in data['forecast']['forecastday']:
            forecast = WeatherResponseModel(
                date= day['date'],
                condition=day['day']['condition']['text'],
                temperature_high=day['day']['maxtemp_c'],
                temperature_low=day['day']['mintemp_c'],
                humidity=day['day']['avghumidity'],
                rain_chance=day['day']['daily_chance_of_rain'],
            )
            forecasts.append(forecast)

        set_cache(cache_key, forecasts, ttl=3600 ) # type: ignore
        return forecasts