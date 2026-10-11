# Yatra Planner

Travel planning API that combines weather, currency, and destination data.

## Run locally

Install dependencies from this directory:

```bash
pip install -r requirements.txt
```

Set a WeatherAPI key in `WEATHER_API_KEY`, then start the app from this directory:

```bash
export WEATHER_API_KEY=your_weatherapi_key
uvicorn app.main:app --reload
```

The API documentation is available at `http://127.0.0.1:8000/docs`.