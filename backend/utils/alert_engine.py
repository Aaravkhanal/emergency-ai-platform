# backend/utils/alert_engine.py

def decide_alert(severity: str, severity_score: float) -> dict:
    """
    Enhanced alert engine with 103 integration
    """
    
    if severity == "HIGH":
        return {
            "level": "EMERGENCY",
            "action": "Alert emergency response team - Call 103",
            "call_103": True,
            "priority": "CRITICAL",
            "estimated_response_time": "5-10 minutes"
        }
    elif severity == "MEDIUM":
        return {
            "level": "WARNING",
            "action": "Monitor situation - Prepare emergency response",
            "call_103": False,
            "priority": "HIGH",
            "estimated_response_time": "15-20 minutes"
        }
    else:
        return {
            "level": "INFO",
            "action": "Log incident - No immediate action required",
            "call_103": False,
            "priority": "LOW",
            "estimated_response_time": "N/A"
        }