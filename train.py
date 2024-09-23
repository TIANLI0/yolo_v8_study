from ultralytics import YOLO

model = YOLO("yolov8n.yaml")

# 读取模型
model = YOLO("yolov8n.pt")

# 训练数据集
results = model.train(data="db/car/data.yaml", epochs=6, workers=0)