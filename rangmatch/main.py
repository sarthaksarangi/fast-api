from contextlib import asynccontextmanager
from fastapi import FastAPI
from database import create_tables
from routes.reviews import router as review_router


@asynccontextmanager
async def lifespan(app:FastAPI):
    print("Lifespan started.")
    create_tables()
    print("Database tables created.")
    yield
    #shutdown: cleanup here
    print("Shuttig down the app.")

    
app = FastAPI(
    title="Rangmatch",
    description="Treatre reviews API for Rangmatch",
    lifespan=lifespan
)

app.include_router(review_router)
@app.get("/")
def root():
    return {"message": "Status: 200"}