# backend/config.py
import os

class Config:
    # Emergency contact configuration for India
    EMERGENCY_NUMBER = "103"  # India Emergency Ambulance
    
    # SMS API Configuration (you'll need to sign up for a service)
    # Popular options: Twilio, MSG91, Fast2SMS, TextLocal
    SMS_API_KEY = os.getenv("SMS_API_KEY", "QFmxRZJvAlBy6IKcL5zsiukaW9dPh43bpjHgfCOMwSoV80nEeTbC7d8DImR6zUOjflhH9NVwAoXsKT4P")
    SMS_API_URL = "https://api.msg91.com/api/v5/flow/"  # Example: MSG91
    
    # Emergency contacts to notify
    EMERGENCY_CONTACTS = [
        "+91X9902835677",  # Replace with actual numbers
        "+9779824066779",
    ]
    
    # Alert threshold - only HIGH severity triggers 103 alert
    ALERT_SEVERITY_THRESHOLD = "HIGH"