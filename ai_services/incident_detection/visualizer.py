# visualizer.py

import cv2
import os
import uuid
from typing import List, Dict

OUTPUT_DIR = "ai_services/incident_detection/outputs"


def draw_detections(
    image,
    detections: List[Dict]
) -> str:
    """
    Draw bounding boxes and labels on image.
    Returns path to saved output image.
    """

    os.makedirs(OUTPUT_DIR, exist_ok=True)

    for det in detections:
        x1, y1, x2, y2 = map(int, det["bbox"][0])
        label = det["label"]
        confidence = det["confidence"]

        # Bounding box
        cv2.rectangle(
            image,
            (x1, y1),
            (x2, y2),
            (0, 0, 255),
            2
        )

        # Label text
        text = f"{label} ({confidence:.2f})"

        cv2.putText(
            image,
            text,
            (x1, max(y1 - 10, 20)),
            cv2.FONT_HERSHEY_SIMPLEX,
            0.6,
            (0, 0, 255),
            2
        )

    # Save image
    filename = f"result_{uuid.uuid4().hex[:8]}.jpg"
    output_path = os.path.join(OUTPUT_DIR, filename)

    cv2.imwrite(output_path, image)

    return output_path
