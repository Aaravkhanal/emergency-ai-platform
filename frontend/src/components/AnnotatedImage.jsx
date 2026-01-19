import "./AnnotatedImage.css";

export default function AnnotatedImage({ url }) {
  if (!url) return null;
  
  // Backend now returns "/outputs/filename.jpg"
  // We just prepend the backend URL
  const imageUrl = `http://127.0.0.1:8000${url}`;
  
  return (
    <div className="annotated-image">
      <h3>📸 Annotated Output</h3>
      <img
        src={imageUrl}
        alt="Annotated detection"
        onError={(e) => {
          console.error("Image failed to load:", imageUrl);
        }}
      />
    </div>
  );
}