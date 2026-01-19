# visualize.py (improved)
import os
import cv2
from detector import IncidentDetector

CLASS_NAMES = {
    0: "bicycle",
    1: "bicycle_bicycle_collision",
    2: "bicycle_vehicle_collision",
    3: "bicycle_pedestrian_collision",
    4: "car",
    5: "car_bicycle_collision",
    6: "car_car_collision",
    7: "car_pedestrian_collision",
    8: "pedestrian",
    9: "other"
}

# simple deterministic color per class
COLOR_MAP = [(0,255,0), (0,128,255), (255,0,0), (255,255,0), (0,255,255),
             (128,0,255), (255,0,128), (0,128,0), (128,128,0), (0,0,255)]

OUT_DIR = "outputs"
os.makedirs(OUT_DIR, exist_ok=True)

def _as_xyxy(bbox):
    # Accept both nested [[x1,y1,x2,y2]] and flat [x1,y1,x2,y2]
    if isinstance(bbox[0], (list, tuple)):
        x1, y1, x2, y2 = bbox[0]
    else:
        x1, y1, x2, y2 = bbox
    return int(x1), int(y1), int(x2), int(y2)

def draw_detections(image_path, output_path=None):
    detector = IncidentDetector()
    detections = detector.detect(image_path)

    image = cv2.imread(image_path)
    h, w = image.shape[:2]

    for det in detections:
        x1, y1, x2, y2 = _as_xyxy(det["bbox"])
        # clamp to image
        x1, y1 = max(0, x1), max(0, y1)
        x2, y2 = min(w-1, x2), min(h-1, y2)

        class_id = det["class_id"]
        confidence = det["confidence"]
        label = f"{CLASS_NAMES.get(class_id, class_id)}: {confidence:.2f}"
        color = COLOR_MAP[class_id % len(COLOR_MAP)]

        # draw bbox
        cv2.rectangle(image, (x1,y1), (x2,y2), color, 2)

        # label background
        (tw, th), _ = cv2.getTextSize(label, cv2.FONT_HERSHEY_SIMPLEX, 0.6, 1)
        cv2.rectangle(image, (x1, max(0, y1-th-8)), (x1+tw+6, y1), color, -1)
        cv2.putText(image, label, (x1+3, max(0, y1-6)),
                    cv2.FONT_HERSHEY_SIMPLEX, 0.6, (0,0,0), 1)

    if output_path is None:
        base = os.path.basename(image_path)
        output_path = os.path.join(OUT_DIR, f"vis_{base}")

    cv2.imwrite(output_path, image)
    print(f"Output saved as {output_path}")
    return output_path

def run_on_folder(folder=".", pattern=(".jpg", ".png")):
    files = [f for f in os.listdir(folder) if f.lower().endswith(pattern)]
    for f in files:
        img_path = os.path.join(folder, f)
        draw_detections(img_path)

if __name__ == "__main__":
    # single image
    draw_detections("frame.jpg")
    # OR to run on val images:
    # run_on_folder("data/val/images")
