import cv2
import os
import glob
from PIL import Image
def make_video(outvid,images, outimg=None, fps=30, size=None,
               is_color=True, format="XVID"):
    from cv2 import VideoWriter, VideoWriter_fourcc, imread, resize
    fourcc = VideoWriter_fourcc(*format)
    vid = None
    for image in images:
        if not os.path.exists(image):
            raise FileNotFoundError(image)
        img = imread(image)
        if vid is None:
            if size is None:
                size = img.shape[1], img.shape[0]
            vid = VideoWriter(outvid, fourcc, float(fps), size, is_color)
        if size[0] != img.shape[1] and size[1] != img.shape[0]:
            img = resize(img, size)
        vid.write(img)
    vid.release()
    return vid
file_list=[]
root="/home/xinzhichao/data2/slamdatasets/zhengziqiang/zheng0807/linshi2/"
lines= open("habr.txt").readlines()
for line in lines:
    tmp=line.strip("\n")
    file_list.append(root+tmp)

make_video('detection.mp4',sorted(file_list))
