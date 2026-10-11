import json
from typing import Annotated, Optional

from fastapi import APIRouter, HTTPException, Query
from fastapi.encoders import jsonable_encoder
from fastapi.responses import StreamingResponse
from ..model import TravelRequest
from ..services.currency import fetch_currency_data
from ..services.places import fetch_places
from ..services.weather import fetch_weather_data


router = APIRouter(
    prefix="/plan",
    tags=["stream"],
)

def format_sse(data: dict, event: Optional[str] = None) -> str:
    """Format data as Server-Sent Events (SSE)"""
    json_data = json.dumps(jsonable_encoder(data))
    return f"data:{json_data}\n\n" if event is None else f"event:{event}\ndata:{json_data}\n\n"


async def stream_generator(travel_request: TravelRequest):
    yield format_sse({"message": "Starting travel plan generation..."}, event="start")
    yield format_sse({"message": "Fetching weather data..."}, event="weather")
    weather_data = await fetch_weather_data(
        destination=travel_request.destination,
        start_date=travel_request.departure_date,
        end_date=travel_request.return_date
    )
    yield format_sse({"message": "Weather data fetched.", "data": weather_data}, event="weather_data")
    places_data = await fetch_places(
        destination=travel_request.destination,
    )
    yield format_sse({"message": "Places data fetched.", "data": places_data},
                        event="places_data")
    currency_data = await fetch_currency_data(base_currency="USD")
    yield format_sse({"message": "Currency data fetched.", "data": currency_data},
                        event="currency_data")
    yield format_sse({"message": "Travel plan generation completed."}, event="end")


@router.get("/stream")
async def stream_travel_plan(
    travel_request: Annotated[TravelRequest, Query()],
):
    if travel_request.departure_date > travel_request.return_date:
        raise HTTPException(status_code=400, detail="Travel Plan departure date can not be more than Travel Date.")
        
    trip_days = (travel_request.return_date - travel_request.departure_date).days
    
    if trip_days >14:
        raise HTTPException(status_code=400, detail="Trip Days can not be greater than 14 days.")
    
    if trip_days < 1:
        raise HTTPException(status_code=400, detail="Trip Days can not be less than 1 day.")

    return StreamingResponse(
        content=stream_generator(travel_request),
        media_type="text/event-stream",
    )