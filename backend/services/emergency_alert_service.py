# backend/services/emergency_alert_service.py
import requests
from backend.config import Config
from datetime import datetime

class EmergencyAlertService:
    """
    Handles 103 emergency alerts for high-severity incidents
    """
    
    @staticmethod
    def send_103_alert(severity: str, severity_score: float, location: str = "Unknown") -> dict:
        """
        Send emergency alert to 103 contacts
        
        Args:
            severity: Severity level (HIGH, MEDIUM, LOW)
            severity_score: Numerical score
            location: Optional location info
            
        Returns:
            dict with alert status
        """
        
        # Only alert for HIGH severity
        if severity != Config.ALERT_SEVERITY_THRESHOLD:
            return {
                "alert_sent": False,
                "reason": f"Severity {severity} below threshold",
                "contacts_notified": 0
            }
        
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        
        message = f"""
🚨 EMERGENCY ALERT 🚨
Severity: {severity}
Score: {severity_score}/5
Location: {location}
Time: {timestamp}

Immediate emergency response required.
Call 103 for ambulance.
        """.strip()
        
        print(f"\n{'='*50}")
        print("📞 103 EMERGENCY ALERT TRIGGERED")
        print(f"{'='*50}")
        print(message)
        print(f"{'='*50}\n")
        
        # In production, send SMS via API
        contacts_notified = EmergencyAlertService._send_sms_alerts(message)
        
        return {
            "alert_sent": True,
            "severity": severity,
            "contacts_notified": contacts_notified,
            "timestamp": timestamp,
            "message": message
        }
    
    @staticmethod
    def _send_sms_alerts(message: str) -> int:
        """
        Send SMS to emergency contacts
        
        Note: You need to configure SMS API (MSG91, Twilio, etc.)
        For now, this is a placeholder that logs to console
        """
        
        # Placeholder - replace with actual SMS API call
        # Example for MSG91:
        # response = requests.post(
        #     Config.SMS_API_URL,
        #     json={
        #         "authkey": Config.SMS_API_KEY,
        #         "mobiles": ",".join(Config.EMERGENCY_CONTACTS),
        #         "message": message,
        #         "sender": "EMRGCY",
        #         "route": "4"
        #     }
        # )
        
        contacts_notified = len(Config.EMERGENCY_CONTACTS)
        
        print(f"📱 SMS Alert would be sent to {contacts_notified} contacts:")
        for contact in Config.EMERGENCY_CONTACTS:
            print(f"   → {contact}")
        
        return contacts_notified