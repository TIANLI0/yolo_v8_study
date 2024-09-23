from ultralytics import YOLO

# 加载模型
model = YOLO("yolov8n.pt")

# 识别图片
results = model(
    source=1,
    device="0",
    show=True,
)
