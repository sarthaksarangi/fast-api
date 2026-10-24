from fastapi import APIRouter, UploadFile, File, HTTPException
from services.image import validate_image, save_image, resize_image
import uuid
from services import vision

router = APIRouter(
    prefix="/analyse",
    tags=["analyse"],
)

async def process_single_image(file: UploadFile):
    """
    Process a single image and return analysis results.
    """
    assert file.content_type is not None
    
    content = await file.read()
    validation_result = validate_image(content, file.content_type) # type: ignore

    if not validation_result["is_valid"]:
        raise HTTPException(status_code=400, detail=validation_result["message"])

    processed = resize_image(content)

    ext = (file.filename or "").split(".")[-1] if "." in (file.filename or "") else "jpg"
    unique_filename = f"{uuid.uuid4()}.{ext}"

    save_image(processed, "uploads", unique_filename)
    result = await vision.analyse_image(processed, file.content_type)

    print(f"Result for {file.filename}: ", result)
    return result

@router.post("/")
async def analyse_image(file: UploadFile = File(...)):
    """
    Endpoint to upload an image and get analysis results.
    """
    if not file.content_type or not file.content_type.startswith('image/'):
        raise HTTPException(status_code=400, detail="Invalid file type. Please upload an image.")

    # Process the image and get analysis results
    analysis_result = await process_single_image(file)

    return {
        "filename": file.filename,
        "content_type": file.content_type,
        "message": "Image uploaded and processed successfully.",
        "analysis_result": analysis_result
    }