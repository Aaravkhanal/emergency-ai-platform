import "./DetectionTable.css";
export default function DetectionTable({ detections }) {
  if (!detections || detections.length === 0) return null;

  return (
    <table border="1">
      <thead>
        <tr>
          <th>Label</th>
          <th>Confidence</th>
          <th>BBox</th>
        </tr>
      </thead>
      <tbody>
        {detections.map((d, i) => (
          <tr key={i}>
            <td>{d.label}</td>
            <td>{d.confidence.toFixed(2)}</td>
            <td>{JSON.stringify(d.bbox)}</td>
          </tr>
        ))}
      </tbody>
    </table>
  );
}
