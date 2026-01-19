const API_BASE = "http://127.0.0.1:8000";

export async function detectIncident(file) {
  const formData = new FormData();
  formData.append("file", file);

  const res = await fetch(`${API_BASE}/detect-incident`, {
    method: "POST",
    body: formData,
  });

  if (!res.ok) throw new Error("Detection failed");

  return res.json();
}
