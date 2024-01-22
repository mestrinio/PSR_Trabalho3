#!/usr/bin/env python3

from ultralytics import YOLO

# Load a pretrained YOLOv8n model
model = YOLO('yolov8n.pt')

source1 = '../person_laptop/Person1.png'
source2 = '../person_laptop/Person2.png'
source3 = '../person_laptop/Person3.png'

# Run inference on 'IMAGE1' with arguments
model.predict(source1, save=True, imgsz=320, conf=0.5, save_txt = True)
model.predict(source2, save=True, imgsz=320, conf=0.5, save_txt = True)
model.predict(source3, save=True, imgsz=320, conf=0.5, save_txt = True)


has_people=[]

path1 = "./runs/detect/predict/labels/Person1.txt"
with open(path1) as f:
    c = f.read()
    if not c:
        has_people.append(False)
    elif c[0] != '0':
        has_people.append(False)
    else:
        has_people.append(True)
        
        

path2 = "./runs/detect/predict/labels/Person2.txt"
with open(path2) as f:
    c = f.read()
    if not c:
        has_people.append(False)
    elif c[0] != '0':
        has_people.append(False)
    else:
        has_people.append(True)
        
        

path3 = "./runs/detect/predict/labels/Person3.txt"
with open(path3) as f:
    c = f.read()
    if not c:
        has_people.append(False)
    elif c[0] != '0':
        has_people.append(False)
    else:
        has_people.append(True)
        
print(has_people)


