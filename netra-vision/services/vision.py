import base64
import json
import os
from openai import OpenAI

client = OpenAI()

response = client.responses.create(
    model="gpt-6-luna",
    input="Write a one-sentence bedtime story about a unicorn.",
)

print(response.output_text)
CROP_ANALYSIS_PROMPT = """
    You are an expert agricultural scientist specializing in crop disease detection.
Analyze this image of a crop/plant and provide a detailed disease assessment.

Provide your analysis as a JSON object with exactly this structure:

{
"crop_detected": "Name of the crop or plant visible in the image",
"severity": "healthy" or "mild" or "moderate" or "severe" or "critical",
"diseases": [
        {
            "name": "Disease name",
            "confidence": 0.0 to 1.0,
            "description": "Brief description of the disease and visible symptoms"
        }
    ],
"treatments": [
        {
            "treatment_name": "Name of treatment",
            "treatment_type": "organic" or "chemical" or "preventive",
            "instructions": "Step by step treatment instructions",
            "urgency": "immediate" or "within_week" or "seasonal"
        }
    ],
    "overall_health": "One sentence summary of plant health",
    "additional_notes": "Any other observations or recommendations"
}
"""

async def analyse_image(image_content: bytes, content_type, ):
    """
    Analyse Image content using Gemini for disease detection
    """
    interaction = client.interactions.create(
        model="gemini-3.8-flash",
        input=[
            {"type": "text", "text": CROP_ANALYSIS_PROMPT},
            {
                "type": "image",
                "data": base64.b64encode(image_content).decode("utf-8"),
                "mime_type": content_type
                
            }
        ],
        response_format={"type": "text", "mime_type": "application/json"},
    )

    response_text = interaction.output_text
    if not response_text:
        raise ValueError("Gemini returned no text for the image analysis.")

    try:
        return json.loads(response_text)
    except json.JSONDecodeError as exc:
        raise ValueError("Gemini returned a response that was not valid JSON.") from exc