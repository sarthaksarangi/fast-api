from fastapi import APIRouter, HTTPException
import asyncio

from ..model import TravelRequest
from ..services.cache import clear_cache, get_cache_stats
from ..services.currency import fetch_currency_data
from ..services.places import fetch_places
from ..services.weather import fetch_weather_data

router = APIRouter(
    prefix="/plan",
    tags=["plan"],
    responses={404: {"description": "Not found"}},
)

@router.post("")
async def create_travel_plan(
    travel_request: TravelRequest
):
    """Aggreagate weather, currency and places data into a single travel plan"""
    if travel_request.departure_date > travel_request.return_date:
        raise HTTPException(status_code=400, detail="Travel Plan departure date can not be more than Travel Date.")
    
    trip_days = (travel_request.return_date - travel_request.departure_date).days

    if trip_days >14:
        raise HTTPException(status_code=400, detail="Trip Days can not be greater than 14 days.")

    if trip_days < 1:
        raise HTTPException(status_code=400, detail="Trip Days can not be less than 1 day.")


    weather_data, places_data, currency_data =   await asyncio.gather(
        fetch_weather_data(
            destination = travel_request.destination,
            start_date = travel_request.departure_date,
            end_date = travel_request.return_date
        ),
        fetch_places(
            destination = travel_request.destination,
        ),
        fetch_currency_data(base_currency="USD")
    )


    return {"message": "Travel plan created successfully",
            "weather_data": weather_data,
            "places_data": places_data,
            "currency_data": currency_data}


@router.get("/cache-stats")
async def cache_stats():
    return get_cache_stats()


@router.delete("/cache")
async def delete_cache():
    cache_stats = get_cache_stats()
    clear_cache()
    return {"message": "Travel plan cache cleared", "cleared_entries": cache_stats["entries"]}



