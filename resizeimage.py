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

def resize_image(image, height , width):
    top, bottom, left, right = (0,0,0,0)

    # 获取图片尺寸
    h, w, _ = image.shape

    # 对于长宽不等的图片，找到最长的一边
    longest_edge = max(h,w)

    # 计算短边需要增加多少像素宽度才能与长边等长(相当于padding，长边的padding为0，短边才会有padding)
    if h < longest_edge:
        dh = longest_edge - h
        top = dh // 2
        bottom = dh - top
    elif w < longest_edge:
        dw = longest_edge - w
        left = dw // 2
        right = dw - left
    else:
        pass # pass是空语句，是为了保持程序结构的完整性。pass不做任何事情，一般用做占位语句。

    # RGB颜色
    BLACK = [0,0,0]
    # 给图片增加padding，使图片长、宽相等
    # top, bottom, left, right分别是各个边界的宽度，cv2.BORDER_CONSTANT是一种border type，表示用相同的颜色填充
    constant = cv2.copyMakeBorder(image, top, bottom, left, right, cv2.BORDER_CONSTANT, value = BLACK)
    # 调整图像大小并返回图像，目的是减少计算量和内存占用，提升训练速度
    return cv2.resize(constant, (height, width))



input_path = "/home/xinzhichao/data2/slamdatasets/zhengziqiang/GH010916/image/" #背景图像路径
output_path =  "/home/xinzhichao/data2/slamdatasets/zhengziqiang/GH010916/image_after/" 
files_im= os.listdir(input_path)#得到文件夹下的所有文件名称
#files_im.sort(key=lambda x:int(x.split('.')[0].split('x')[1]))

#change_imagename() #修改图像文件名,之前文件夹中图像文件名的命名方式是类别加数字，更改后是纯数字命名
for file_name in tqdm(files_im): #遍历文件夹
    image =  cv2.imread(input_path + str(file_name))

    image = cv2.resize(image, (640, 480))
    cv2.imwrite(output_path+ str(file_name) , image)
