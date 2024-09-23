import json  
import os  

# 指定包含JSON文件的文件夹路径  
json_folder_path = 'db/strit/train'  

# 输出YOLO数据集文件夹路径  
yolo_folder_path = 'db/strit/trains'  

# 类别
class_list = ['p', 'car', 'bicycle', ...] 
class_id_list = list(range(len(class_list)))  
os.makedirs(yolo_folder_path, exist_ok=True)  

# 遍历JSON文件夹  
for file_name in os.listdir(json_folder_path):  
    if file_name.endswith('.json'):  # 检查文件扩展名  
        json_file_path = os.path.join(json_folder_path, file_name)  
        with open(json_file_path, 'r') as f:  
            data = json.load(f)  
            yolo_file_path = os.path.join(yolo_folder_path, file_name.replace('.json', '.txt'))  
             
            with open(yolo_file_path, 'w') as yolo_f:  
                for shape in data['shapes']:  
                    label = shape['label']  
                    points = shape['points']  
                    x_center = (points[0][0] + points[2][0]) / 2  
                    y_center = (points[0][1] + points[2][1]) / 2  
                    width = points[2][0] - points[0][0]  
                    height = points[2][1] - points[0][1]  
                    
                    # 将坐标转换为YOLO格式  
                    x_center = x_center / data['imageWidth']  
                    y_center = y_center / data['imageHeight']  
                    width = width / data['imageWidth']  
                    height = height / data['imageHeight']  
                    
                    # 找到对应的类别ID  
                    class_id = class_id_list[class_list.index(label)]   
                    yolo_f.write(f"{class_id} {x_center:.6f} {y_center:.6f} {width:.6f} {height:.6f}/n")  

print("YOLO数据集格式已生成.")