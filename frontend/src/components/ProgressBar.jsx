import "./ProgressBar.css";

export default function ProgressBar({ current, total }) {
  const percentage = total > 0 ? (current / total) * 100 : 0;
  
  return (
    <div className="progress-container">
      <div className="progress-bar">
        <div 
          className="progress-fill" 
          style={{ width: `${percentage}%` }}
        ></div>
      </div>
      <p className="progress-text">
        ⏳ Processing image {current} of {total}...
      </p>
    </div>
  );
}