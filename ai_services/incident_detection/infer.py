# infer.py

from detector import IncidentDetector

def main():
    detector = IncidentDetector()

    detections = detector.detect("frame.jpg")

    print("Detections:")
    for d in detections:
        print(d)

if __name__ == "__main__":
    main()
