import "./SeverityCard.css";
export default function SeverityCard({ severity, score }) {
  if (!severity) return null;

  return (
    <div style={{ border: "2px solid red", padding: 16 }}>
      <h2>Severity: {severity}</h2>
      <p>Score: {score}</p>
    </div>
  );
}
