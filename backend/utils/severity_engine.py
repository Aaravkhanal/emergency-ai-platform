# severity_engine.py

from typing import List, Dict


# Weight mapping for incident types
SEVERITY_WEIGHTS = {
    "car_collision": 3.0,
    "major_accident": 4.0,
    "fire": 5.0,
    "explosion": 5.0
}

CRITICAL_LABELS = {"major_accident", "fire", "explosion"}


def compute_severity(detections: List[Dict]) -> Dict:
    """
    Compute severity based on detected incidents.
    """

    if not detections:
        return {
            "severity": "LOW",
            "severity_score": 0.0,
            "severity_reason": ["No incidents detected"]
        }

    score = 0.0
    reasons = []
    critical_found = False

    for det in detections:
        label = det["label"]
        confidence = det["confidence"]

        weight = SEVERITY_WEIGHTS.get(label, 1.0)
        contribution = confidence * weight
        score += contribution

        reasons.append(
            f"Detected {label} with confidence {confidence:.2f} (weight {weight})"
        )

        if label in CRITICAL_LABELS:
            critical_found = True

    # Multiple incident penalty
    if len(detections) > 1:
        score += 0.5
        reasons.append(f"Multiple incidents detected ({len(detections)} total)")

    # Base severity mapping
    if score < 1.5:
        severity = "LOW"
    elif score < 3.5:
        severity = "MEDIUM"
    else:
        severity = "HIGH"

    # Critical override
    if critical_found:
        severity = "HIGH"
        reasons.append("Critical incident detected → severity escalated to HIGH")

    return {
        "severity": severity,
        "severity_score": round(score, 2),
        "severity_reason": reasons
    }
