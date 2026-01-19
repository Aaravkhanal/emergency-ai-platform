print("train.py started")# training start vayo aba yolo bata train garera yo chai 
#configuration haru set garne

from ultralytics import YOLO

print("Ultralytics imported successfully")

def train():
    print("Starting YOLO training...")
    model = YOLO("yolov8n.pt")

    model.train(
        data="data.yaml",
        epochs=10,
        imgsz=640,
        batch=8,
        device="cpu"
    )

if __name__ == "__main__":
    train()
