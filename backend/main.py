from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from fastapi.middleware.cors import CORSMiddleware  # ✅ ADD THIS
from backend.routes.incident import router as incident_router
import os

app = FastAPI(title="Emergency AI Platform")

# ✅ ADD CORS MIDDLEWARE (put this right after creating app)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173"],  # Your frontend URL
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# 🔹 Absolute path to outputs folder
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
OUTPUTS_DIR = os.path.join(
    BASE_DIR,
    "ai_services",
    "incident_detection",
    "outputs"
)

# 🔹 Serve annotated images (you have this twice - remove the duplicate below)
app.mount(
    "/outputs",
    StaticFiles(directory=OUTPUTS_DIR),
    name="outputs"
)

# 🔹 API routes
app.include_router(incident_router)

@app.get("/")
def root():
    return {"status": "Emergency AI Platform running"}