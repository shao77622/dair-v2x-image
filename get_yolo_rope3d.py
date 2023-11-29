# -*- coding: utf-8 -*-
import json
from tqdm import tqdm 
import os 
import pdb
w = 1920
h = 1080
label_path='/Users/shaoben/Documents/dataset/DAIR-V2X/Rope3D/training/label_2'
label_path_yolo='/Users/shaoben/Documents/dataset/DAIR-V2X/Rope3D/training/label_yolo'
txts = os.listdir(label_path)
type_dict = {
    "pedestrian": 1,
    "motorcyclist": 2,
    "car": 0,
    "cyclist": 2,
    "tricyclist": 2,
    "van": 0,
    "truck": 0,
    "bus": 0,
    "barrow": 2
}
for j in tqdm(txts):
    j_file = os.path.join(label_path,j)
    with open(j_file, 'r') as f:
        data = f.readlines()

    txt_file = os.path.join(label_path_yolo,j.split('.')[0]+'.txt')

    # ��txt�������
    with open(txt_file, 'w') as f:
        for line in data:
            item = line.split(" ")
            # ��type
            type_ = item[0]
            if type_ != 'trafficcone' and type_ != 'unknown_unmovable' and type_ != 'unknowns_movable':
                # ��2d_box
                type_ = type_dict[type_]
                xmin = float(item[4])
                ymin = float(item[5])
                xmax = float(item[6])
                ymax = float(item[7])
                # ����
                x = (xmin + xmax) / (2 * w)
                y = (ymin + ymax) / (2 * h)
                width = (xmax - xmin) / w
                height = (ymax - ymin) / h
                # ���txt��
                f.write(f'{type_} {x:.6f} {y:.6f} {width:.6f} {height:.6f}\n')

