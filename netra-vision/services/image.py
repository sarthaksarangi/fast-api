from PIL import Image 
import io
import os


ALLOWED_IMAGES_TYPES = ["image/jpeg", "image/png", "image/gif", "image/bmp", "image/webp"]
MAX_IMAGE_DIMENSION = 1024  # Maximum width or height in pixels


def validate_image(content: bytes, content_type: str ) -> dict:
    """
    Validate the uploaded image based on its content type and size.
    """
    if content_type not in ALLOWED_IMAGES_TYPES:
        return {"is_valid": False, "message": "Invalid image type"}

    if len(content) > 5 * 1024 * 1024:  # Limit to 5MB
        return {"is_valid": False, "message": "Image size exceeds limit"}
    
    if len(content) > 5 * 1024 * 1024:  # Limit to 5MB
        return {"is_valid": False, "message": "Image size exceeds limit"}

    size_mb = len(content) / (1024 * 1024)

    if size_mb > 15:
        return {"is_valid": False, "message": "Image size exceeds limit"}

    image = Image.open(io.BytesIO(content))
    width, height = image.size
    
    return {"is_valid": True, "message": "Image is valid", "width": width, "height": height, "size_mb": size_mb}

def resize_image(content: bytes) -> bytes:
    """
    Resize the image to fit within the specified dimensions while maintaining aspect ratio.
    """
    image = Image.open(io.BytesIO(content))
    width, height = image.size

    if width > height:
        new_width = MAX_IMAGE_DIMENSION
        new_height = int((new_width / width) * height)
    else:
        new_height = MAX_IMAGE_DIMENSION
        new_width = int((new_height / height) * width)

    resized_image = image.resize((new_width, new_height), Image.Resampling.LANCZOS)
    
    output = io.BytesIO()
    resized_image.save(output, format=image.format)
    return output.getvalue()

def save_image(content: bytes, upload_path: str, filename: str) -> str:
    """
    Save the image to the specified path.
    """
    os.makedirs(upload_path, exist_ok=True)
    file_path = os.path.join(upload_path, filename)

    with open(file_path, "wb") as f:
        f.write(content)
        
    return file_path