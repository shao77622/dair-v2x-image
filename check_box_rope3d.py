import json
from PIL import Image, ImageDraw
import pdb
# 读取JSON文件
with open('/Users/shaoben/Documents/dataset/DAIR-V2X/Rope3D/validation/label_2/148709_sj8fas2e152d20211124air_420_1637216131_1637218737_1_obstacle.txt') as f:
    data = f.readlines()
# 读取对应的图像文件
image_filename ='/Users/shaoben/Documents/dataset/DAIR-V2X/Rope3D/validation-image_2/148709_sj8fas2e152d20211124air_420_1637216131_1637218737_1_obstacle.jpg'  # 假设图像文件名与JSON文件名一致，并且为jpg格式
image = Image.open(image_filename)

for line in data:
    item = line.split(" ")
    # 提取2d_box的坐标
    xmin = float(item[4])
    ymin = float(item[5])
    xmax = float(item[6])
    ymax = float(item[7])

    # 在图像上绘制矩形框
    draw = ImageDraw.Draw(image)
    draw.rectangle([(xmin, ymin), (xmax, ymax)], outline='red')
    # pdb.set_trace()
# 保存标注后的图像
annotated_image_filename =  '_annotated.jpg'
image.save(annotated_image_filename)
