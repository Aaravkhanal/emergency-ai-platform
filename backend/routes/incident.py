from fastapi import APIRouter, UploadFile, File, HTTPException
from backend.services.incident_service import detect_incident

router = APIRouter()


@router.post("/detect-incident")
async def detect_incident_api(file: UploadFile = File(...)):
    """
    Accepts an image file and returns:
    - severity
    - severity_score
    - severity_reason
    - detections
    - annotated_image_url
    """

    if not file.content_type.startswith("image/"):
        raise HTTPException(status_code=400, detail="Only image files are allowed")

    image_bytes = await file.read()

    if not image_bytes:
        raise HTTPException(status_code=400, detail="Empty image uploaded")

    result = detect_incident(image_bytes)

    if not result:
        raise HTTPException(status_code=500, detail="Incident detection failed")

    return result
