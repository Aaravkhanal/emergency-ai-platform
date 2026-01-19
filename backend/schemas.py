# backend/schemas.py
from pydantic import BaseModel
from typing import List, Optional

class Detection(BaseModel):
    class_id: int
    label: str
    confidence: float
    bbox: List[List[float]]

class Alert(BaseModel):
    level: str
    action: str
    call_103: bool
    priority: str
    estimated_response_time: str

class EmergencyAlert(BaseModel):
    alert_sent: bool
    severity: Optional[str] = None
    contacts_notified: Optional[int] = None
    timestamp: Optional[str] = None
    message: Optional[str] = None
    reason: Optional[str] = None

class IncidentResponse(BaseModel):
    severity: str
    severity_score: float
    severity_reason: List[str]
    detections: List[Detection]
    alert: Alert
    emergency_alert: Optional[EmergencyAlert] = None  # ✅ NEW
    annotated_image_url: str