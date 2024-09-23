from ultralytics import YOLO

# 加载模型
model = YOLO("runs/detect/train13/weights/best.pt")

# 识别图片
results = model(
    source="val/324554841-1-16.mp4",
    device="0",
    show=True,
)
