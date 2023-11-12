from ultralytics import YOLO

# Load a model
model = YOLO('yolov8n-pose.pt')  # load an official model

# Predict with the model
results = model(source=0, show=True, device='cpu')