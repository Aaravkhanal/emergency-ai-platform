import { useState } from "react";
import UploadForm from "./components/UploadForm";
import ResultCard from "./components/ResultCard";
import ProgressBar from "./components/ProgressBar";
import "./App.css";

export default function App() {
  const [results, setResults] = useState([]); // ✅ Changed to array
  const [loading, setLoading] = useState(false);
  const [progress, setProgress] = useState({ current: 0, total: 0 });

  const detectIncident = async (files) => {
    setLoading(true);
    setResults([]);
    setProgress({ current: 0, total: files.length });

    const allResults = [];

    for (let i = 0; i < files.length; i++) {
      const file = files[i];
      setProgress({ current: i + 1, total: files.length });

      try {
        const formData = new FormData();
        formData.append("file", file);

        // Add minimum delay for progress bar visibility
        const [res] = await Promise.all([
          fetch("http://127.0.0.1:8000/detect-incident", {
            method: "POST",
            body: formData,
          }),
          new Promise(resolve => setTimeout(resolve, 1500))
        ]);

        const data = await res.json();
        console.log(`AI RESPONSE ${i + 1}:`, data);
        allResults.push(data);
      } catch (err) {
        console.error(`Detection failed for image ${i + 1}`, err);
        alert(`Error processing image ${i + 1}`);
      }
    }

    setResults(allResults);
    setLoading(false);
  };

  const clearResults = () => {
    setResults([]);
  };

  const removeResult = (index) => {
    setResults(results.filter((_, i) => i !== index));
  };

  return (
    <div className="app-container">
      <h1>🚨 Emergency AI Platform</h1>
      <UploadForm onDetect={detectIncident} />

      {loading && (
        <ProgressBar 
          current={progress.current} 
          total={progress.total} 
        />
      )}

      {results.length > 0 && (
        <>
          <div style={{ textAlign: "center", marginBottom: "30px" }}>
            <button
              onClick={clearResults}
              style={{
                background: "linear-gradient(135deg, #ef4444, #dc2626)",
                padding: "12px 24px",
                borderRadius: "8px",
                border: "none",
                color: "white",
                fontWeight: "600",
                cursor: "pointer",
                fontSize: "16px"
              }}
            >
              🗑️ Clear All Results ({results.length})
            </button>
          </div>

          {results.map((result, index) => (
            <ResultCard
              key={index}
              result={result}
              index={index}
              onRemove={removeResult}
            />
          ))}
        </>
      )}
    </div>
  );
}