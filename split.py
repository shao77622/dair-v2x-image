
import os

orin_img_path='/Users/shaoben/Documents/dataset/DAIR-V2X/single-infrastructure-side/single-infrastructure-side-image'
orin_img_dir=os.listdir(orin_img_path)
orin_lb_path='/Users/shaoben/Documents/dataset/DAIR-V2X/single-infrastructure-side/single-infrastructure-side-label/label_yolo'
orin_lb_dir=os.listdir(orin_lb_path)
##train
train_img_path = "/Users/shaoben/Documents/dataset/DAIR-V2X/single-infrastructure-side/train_dair_v2x/images"
train_img_dir = os.listdir(train_img_path)  # image
train_lb_path="/Users/shaoben/Documents/dataset/DAIR-V2X/single-infrastructure-side/train_dair_v2x/labels"
train_lb_dir = os.listdir(train_lb_path)

##val
val_img_path = "/Users/shaoben/Documents/dataset/DAIR-V2X/single-infrastructure-side/val_dair_v2x/images"
val_img_dir = os.listdir(val_img_path)  # image
val_lb_path="/Users/shaoben/Documents/dataset/DAIR-V2X/single-infrastructure-side/val_dair_v2x/labels"
val_lb_dir = os.listdir(val_lb_path)

orin_count=len(orin_img_dir)

orin_img_dir = sorted(orin_img_dir)
# val_lb_dir = sorted(val_lb_dir)

for i in range(orin_count):
    if i % 10 ==0:
        cmd = "mv {} {}".format(os.path.join(orin_img_path, orin_img_dir[i]), val_img_path)
        print(cmd)
        os.system(cmd)
        cmd = "mv {} {}".format(os.path.join(orin_lb_path, orin_img_dir[i].split(".")[0]+".txt"), val_lb_path)
        print(cmd)
        os.system(cmd)
    else:
        cmd = "mv {} {}".format(os.path.join(orin_img_path, orin_img_dir[i]), train_img_path)
        print(cmd)
        os.system(cmd)
        cmd = "mv {} {}".format(os.path.join(orin_lb_path, orin_img_dir[i].split(".")[0]+".txt"), train_lb_path)
        print(cmd)
        os.system(cmd)



