# detector.py
import cv2
import numpy as np
from typing import List, Dict, Tuple

from ai_services.incident_detection.model import load_model
from ai_services.incident_detection.config import CONFIDENCE_THRESHOLD, CLASS_NAMES
from ai_services.incident_detection.visualizer import draw_detections


class IncidentDetector:
    def __init__(self):
        self.model = load_model()

    def detect(self, image_bytes: bytes) -> Tuple[List[Dict], str]:
        """
        Detect incidents from raw image bytes.
        Returns:
            detections (list of dicts)
            output_image_path (str)
        """

        # Decode image bytes to OpenCV image
        np_arr = np.frombuffer(image_bytes, np.uint8)
        image = cv2.imdecode(np_arr, cv2.IMREAD_COLOR)

        if image is None:
            raise ValueError("Invalid image data received")

        # Run YOLO inference
        results = self.model(image, imgsz=640)[0]

        detections: List[Dict] = []

        for box in results.boxes:
            conf = float(box.conf)
            if conf < CONFIDENCE_THRESHOLD:
                continue

            class_id = int(box.cls)
            label = CLASS_NAMES.get(class_id, f"class_{class_id}")

            detections.append({
                "class_id": class_id,
                "label": label,
                "confidence": conf,
                "bbox": box.xyxy.tolist()
            })

        # Draw and save annotated image
        output_path = draw_detections(image, detections)

        return detections, output_path
