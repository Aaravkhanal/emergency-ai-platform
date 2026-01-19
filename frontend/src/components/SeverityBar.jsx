import "./SeverityCard.css";

export default function SeverityCard({ severity, score }) {
  if (!severity) return null;
  return (
    <div className="severity-card">
      <h2>⚠️ Severity: {severity}</h2>
      <p>Risk Score: {score}/5</p>
    </div>
  );
}