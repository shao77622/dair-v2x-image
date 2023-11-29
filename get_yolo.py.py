# -*- coding: utf-8 -*-
import json
from tqdm import tqdm 
import os 
import pdb
w = 1920
h = 1080
label_path='/Users/shaoben/Documents/dataset/DAIR-V2X/DAIR-V2X-I/single-infrastructure-side-label/label/camera'
label_path_yolo='/Users/shaoben/Documents/dataset/DAIR-V2X/DAIR-V2X-I/single-infrastructure-side-label/label_yolo'
jsons = os.listdir(label_path)
type_dict = {
#    "Pedestrian": 1,
#    "Motorcyclist": 2,
    "Car": 0,
#    "Cyclist": 2,
#    "Tricyclist": 2,
    "Van": 0,
    "Truck": 0,
    "Bus": 0,
#    "Barrowlist": 2
}
for j in tqdm(jsons):
    j_file = os.path.join(label_path,j)
    with open(j_file, 'r') as f:
        data = json.load(f)

    txt_file = os.path.join(label_path_yolo,j.split('.')[0]+'.txt')

    # ��txt�������
    with open(txt_file, 'w') as f:
        for item in data:
            # ��type
            type_ = item['type']
            if type_ in type_dict.keys():
                # ��2d_box
                type_ = type_dict[type_]
                box = item['2d_box']
                # ����
                x = (float(box['xmin']) + float(box['xmax'])) / (2 * w)
                y = (float(box['ymin']) + float(box['ymax'])) / (2 * h)
                width = (float(box['xmax']) - float(box['xmin'])) / w
                height = (float(box['ymax']) - float(box['ymin'])) / h
                # ���txt��
                f.write(f'{type_} {x:.6f} {y:.6f} {width:.6f} {height:.6f}\n')

