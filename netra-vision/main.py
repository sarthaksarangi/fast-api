from fastapi import FastAPI
from dotenv import load_dotenv

load_dotenv()  # Load environment variables from .env file

from routes.analyse import router as analyse_router

app = FastAPI(
    title = "Netra Vision API",
    description = "This is a FastAPI application for Netra Vision.",
    version = "1.0.0",
)



@app.get("/")
async def root():
    return {
        "message": "Welcome to Netra Vision API!",
        "endpoints": {
            "POST /analyse": "Upload an image and get analysis results.",
            "POST /analyse/batch": "Upload multiple images and get analysis results for each.",
            "GET /analyse": "Retrieve analysis results for a previously uploaded image using its ID.",
            "GET /analyse/{image_id}": "Retrieve analysis results for a specific image using its ID.",
            }}

app.include_router(analyse_router)