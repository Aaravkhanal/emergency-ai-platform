import "./ExplainabilityTable.css";
export default function ExplainabilityPanel({ reasons }) {
  if (!reasons) return null;

  return (
    <div>
      <h3>AI Decision Explanation</h3>
      <ul>
        {reasons.map((r, i) => (
          <li key={i}>{r}</li>
        ))}
      </ul>
    </div>
  );
}
