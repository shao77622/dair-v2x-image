import json
from PIL import Image, ImageDraw
import pdb
# 读取JSON文件
with open('/Users/shaoben/Documents/dataset/DAIR-V2X/single-infrastructure-side/label/camera/000000.json') as f:
    data = json.load(f)
# 读取对应的图像文件
image_filename ='/Users/shaoben/Documents/dataset/DAIR-V2X/single-infrastructure-side-image/000000.jpg'  # 假设图像文件名与JSON文件名一致，并且为jpg格式
image = Image.open(image_filename)

# 遍历每个JSON对象
for item in data:
    # 提取2d_box的坐标
    box = item['2d_box']
    xmin = float(box['xmin'])
    ymin = float(box['ymin'])
    xmax = float(box['xmax'])
    ymax = float(box['ymax'])
     
    # 在图像上绘制矩形框
    draw = ImageDraw.Draw(image)
    draw.rectangle([(xmin, ymin), (xmax, ymax)], outline='red')
    #pdb.set_trace()
# 保存标注后的图像
annotated_image_filename =  '_annotated.jpg'
image.save(annotated_image_filename)
