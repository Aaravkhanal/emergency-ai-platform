import "./AlertBanner.css";

export default function AlertBanner({ alert, emergencyAlert }) {
  if (!alert) return null;
  
  const isEmergency = alert.call_103;
  
  return (
    <div className={`alert-banner ${isEmergency ? 'emergency' : 'warning'}`}>
      <div className="alert-content">
        <div className="alert-icon">
          {isEmergency ? '🚨' : '⚠️'}
        </div>
        <div className="alert-text">
          <strong>{alert.level}:</strong> {alert.action}
          <div className="alert-meta">
            Priority: {alert.priority} | Response Time: {alert.estimated_response_time}
          </div>
          
          {emergencyAlert && emergencyAlert.alert_sent && (
            <div className="emergency-status">
              ✅ 103 Emergency Alert Sent to {emergencyAlert.contacts_notified} contacts at {emergencyAlert.timestamp}
            </div>
          )}
        </div>
      </div>
    </div>
  );
}