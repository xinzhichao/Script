import cv2
import numpy as np
import copy
from lxml.etree import Element, SubElement, tostring, ElementTree
 
import xml.etree.ElementTree as ET
import pickle
import os
from os import listdir, getcwd
from os.path import join
from tqdm import tqdm
import random
import glob
classes = ["holothurian","echinus","starfish","scallop"]  #类别


def change_imagename():
    cwd = "/home/xinzhichao/data/datapre/scallop/"
    res=os.listdir(cwd)
    global num
    for i in res:
        num = num + 1
        if ".jpg" in i:
            os.rename(os.path.join(cwd,i),os.path.join(cwd,str(num)+".jpg"))


def image_result(file_name):
    image_id = file_name.split('.')[0]
    path_obj = "/home/xinzhichao/data/datapre/scallop/"#将要粘贴图像路径
    path_im = "/home/xinzhichao/data/datapre/image/" #背景图像路径
    xml_path ="/home/xinzhichao/data/datapre/boxs/%s.xml" %(image_id)
    in_file = open(xml_path)
    image_path = path_im + str(image_id) + ".jpg" #从原始路径读取图像文件

    tree=ET.parse(in_file)
    root = tree.getroot()
    size = root.find('size')  
    mixed_clone = cv2.imread(image_path)
    for obj in root.iter('object'):
        cls = obj.find('name').text  #每一个类别
        if cls not in classes :
            continue
        xmlbox = obj.find('bndbox')   
        b = (float(xmlbox.find('xmin').text), float(xmlbox.find('xmax').text), float(xmlbox.find('ymin').text), float(xmlbox.find('ymax').text))
        if cls == "echinus":
            obj.find('name').text =  "scallop"
            tree.write(xml_path)

            # #先用周围环境进行泊松融合，使得需要泊松填充的位置原来物种的影响降低到最低
            # objs = mixed_clone[ int(b[2]):int(b[3]) , int(b[0]):int(b[1])]
            # objs[ :, :] = mixed_clone[int(b[2]-50) , int(b[0]-50)]
            # # MIXED_CLONE
            # objs = cv2.resize(objs, (int(b[1])-int(b[0]) , int(b[3])-int(b[2]) ), cv2.INTER_CUBIC)
            # mask = 1 * np.ones(objs.shape, objs.dtype)
            # center = ( int(b[0]+((b[1]-b[0])/2)) , int(b[2]+((b[3]-b[2])/2))  )
            # mixed_clone = cv2.seamlessClone(objs, mixed_clone, mask, center, cv2.MIXED_CLONE)

            #将需要填充的物种进行泊松融合
            objs = cv2.imread(path_obj  + str(random.randint(1, 846)) +".jpg")
            objs = cv2.resize(objs, (int(b[1])-int(b[0]) , int(b[3])-int(b[2]) ), cv2.INTER_CUBIC)
            mask = 255 * np.ones(objs.shape, objs.dtype)
            # The location of the center of the obj in the im
            #center = (int(b[2]+((b[3]-b[2])/2)), int(b[0]+((b[1]-b[0])/2)))
            center = ( int(b[0]+((b[1]-b[0])/2)) , int(b[2]+((b[3]-b[2])/2))  )
            # Seamlessly clone obj into im and put the results in output
            #normal_clone = cv2.seamlessClone(objs, normal_clone, mask, center, cv2.NORMAL_CLONE)
            mixed_clone = cv2.seamlessClone(objs, mixed_clone, mask, center, cv2.NORMAL_CLONE)
            break

    cv2.imwrite("/home/xinzhichao/data/datapre/bosongresult/"+ str(image_id ) + ".jpg",mixed_clone)

num = 0
path_im = "/home/xinzhichao/data/datapre/image/" #背景图像路径
files_im= os.listdir(path_im)#得到文件夹下的所有文件名称
files_im.sort(key=lambda x:int(x.split('.')[0].split('x')[1]))

#change_imagename() #修改图像文件名,之前文件夹中图像文件名的命名方式是类别加数字，更改后是纯数字命名
for file_name in tqdm(files_im): #遍历文件夹
    image_result(file_name)

    




