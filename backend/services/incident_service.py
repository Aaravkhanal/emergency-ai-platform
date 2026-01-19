# backend/services/incident_service.py
import uuid
import os
from ai_services.incident_detection.detector import IncidentDetector
from backend.utils.severity_engine import compute_severity
from backend.utils.alert_engine import decide_alert
from backend.services.emergency_alert_service import EmergencyAlertService

# Initialize detector once
detector = IncidentDetector()

def detect_incident(image_bytes: bytes) -> dict:
    """
    Main incident detection pipeline with 103 integration
    """
    # Step 1: Run detection
    detections, annotated_image_path = detector.detect(image_bytes)
    
    # Step 2: Compute severity
    severity_result = compute_severity(detections)
    
    # Step 3: Decide alert action
    alert = decide_alert(
        severity=severity_result["severity"],
        severity_score=severity_result["severity_score"]
    )
    
    # Step 4: Send 103 alert if HIGH severity
    emergency_alert_status = None
    if alert.get("call_103", False):
        emergency_alert_status = EmergencyAlertService.send_103_alert(
            severity=severity_result["severity"],
            severity_score=severity_result["severity_score"],
            location="Detected via AI Platform"  # You can add GPS coordinates here
        )
    
    # Step 5: Extract filename for URL
    filename = os.path.basename(annotated_image_path)
    
    # Step 6: Final API response
    return {
        "severity": severity_result["severity"],
        "severity_score": severity_result["severity_score"],
        "severity_reason": severity_result["severity_reason"],
        "alert": alert,
        "emergency_alert": emergency_alert_status,  # ✅ NEW
        "annotated_image_url": f"/outputs/{filename}",
        "detections": detections
    }