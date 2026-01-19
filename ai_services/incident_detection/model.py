# ai_services/incident_detection/model.py
from ultralytics import YOLO
from ai_services.incident_detection.config import MODEL_PATH


def load_model():
    return YOLO(MODEL_PATH)
