import "./UploadForm.css";
import { useState } from "react";

export default function UploadForm({ onDetect }) {
  const [files, setFiles] = useState([]);

  const handleFileChange = (e) => {
    const selectedFiles = Array.from(e.target.files); // ✅ Convert to array
    setFiles(selectedFiles);
    console.log("Selected files:", selectedFiles.length); // Debug
  };

  const submit = (e) => {
    e.preventDefault();
    if (files.length > 0) {
      console.log("Submitting files:", files); // Debug
      onDetect(files); // Pass all files
      setFiles([]); // Clear after submit
      e.target.reset(); // Reset form
    }
  };

  return (
    <form onSubmit={submit} className="upload-form">
      <input 
        type="file" 
        onChange={handleFileChange}
        accept="image/*"
        multiple
      />
      <span className="file-count">
        {files.length > 0 ? `${files.length} file(s) selected` : "No files selected"}
      </span>
      <button type="submit" disabled={files.length === 0}>
        Detect {files.length > 0 ? `${files.length} ` : ''}Incident{files.length !== 1 ? 's' : ''}
      </button>
    </form>
  );
}