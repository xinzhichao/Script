import copy
from lxml.etree import Element, SubElement, tostring, ElementTree

import xml.etree.ElementTree as ET
import pickle
import os
from os import listdir, getcwd
from os.path import join
import glob
import cv2

#将裁剪后的图像粘贴到原图中


def convert_annotation():
    #holothurian - echinus - starfish - scallop - holothurian
    in_file = '/home/xinzhichao/data2/CLionProjects/Dual_SLAM(复件)/Trajectory_Mono.txt'
    xmls = glob.glob(in_file)

    f = open(in_file, 'r+', encoding='utf-8')
    all_the_lines = f.readlines()
    f.seek(0)
    f.truncate()
    global num 
    global nums
    for line in all_the_lines:
        num = num +1
        nums = nums +1
        print("frame"+str(num).zfill(6)+".png")
        #print(num+'.'+str(0))
        #line = line.replace(("frame"+str(num).zfill(6)+".png"), str(nums))
        line = line.replace((str(nums)+".000000"),(str(num)+".0"))
        #line = line.replace(',', ' ')
        f.write(line)
    f.close()


num = 4888
nums = 87
#for image_id in list_file_train:
# list_file_train.write('/home/xinzhichao/Code/PyTorch-YOLOv3/data/customurpc/image/%s.jpg\n'%(image_id))  #应该是没啥用
convert_annotation()   
    #image_convert(image_id)
# from tqdm import tqdm

# path = "/home/xinzhichao/data/train_mix/addd/boxrename2" #文件夹目录
# files= os.listdir(path) #得到文件夹下的所有文件名称
# for file_name in tqdm(files): #遍历文件夹
#     convert_annotation3(file_name.split('.')[0])   
#     #image_convert(file_name.split('.')[0])
