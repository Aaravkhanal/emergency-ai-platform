# config.py
import os

MODEL_PATH = "ai_services/incident_detection/runs/detect/train/weights/best.pt"
CONFIDENCE_THRESHOLD = 0.4
IMAGE_SIZE = 640

OUTPUT_DIR = "ai_services/incident_detection/outputs"
os.makedirs(OUTPUT_DIR, exist_ok=True)

CLASS_NAMES = {
    4: "car_collision",
    6: "major_accident"
}
