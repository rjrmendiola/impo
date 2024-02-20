from ultralytics import YOLO

def get_model():
    model = YOLO("yolov8m.pt")
    return model