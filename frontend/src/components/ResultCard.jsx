import SeverityCard from "./SeverityCard";
import DetectionTable from "./DetectionTable";
import AnnotatedImage from "./AnnotatedImage";
import AlertBanner from "./AlertBanner";  // ✅ ADD THIS
import "./ResultCard.css";

export default function ResultCard({ result, index, onRemove }) {
  return (
    <div className="result-card">
      <div className="result-header">
        <h2>📸 Image {index + 1}</h2>
        <button onClick={() => onRemove(index)} className="remove-btn">
          ✕ Remove
        </button>
      </div>
      
      {/* ✅ ADD ALERT BANNER */}
      {result.alert && (
        <AlertBanner 
          alert={result.alert} 
          emergencyAlert={result.emergency_alert}
        />
      )}
      
      <SeverityCard
        severity={result.severity}
        score={result.severity_score}
      />
      
      <DetectionTable detections={result.detections} />
      
      {result.annotated_image_url && (
        <AnnotatedImage url={result.annotated_image_url} />
      )}
    </div>
  );
}