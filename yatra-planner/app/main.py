from fastapi import FastAPI
from .routes import planner as planner_router
from .routes import stream as stream_router

app = FastAPI(
    title="Yatra Planner",
    description="Aggregate travel planning and itinerary management tool for travelers",
)

app.include_router(planner_router.router)
app.include_router(stream_router.router)

@app.get("/")
async def root():
    return {"app": "Welcome to Yatra Planner!",
            "version": "1.0.0",
            "endpoints":{
                "POST /plan": "Create a new travel plan (Aggregated)",
                "GET /plan/stream":"Stream a travel plan (SSE)",
                "GET /plan/cache-stats":"View the cache statistics",
                "DELETE /plan/cache":"Delete the cache for travel plans",
            }
            }

