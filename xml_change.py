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

classes = ["holothurian","echinus","starfish","scallop"]  #类别
n = 5000
def convert_annotation1(image_id):
    #holothurian - echinus - starfish - scallop - holothurian
    in_file = '/home/xinzhichao/data/dataGAN/data/result/boxxml/%s.xml'%(image_id)
    xmls = glob.glob(in_file)
    for one_xml in xmls:
        print(one_xml)
        f = open(one_xml, 'r+', encoding='utf-8')
        all_the_lines = f.readlines()
        f.seek(0)
        f.truncate()
        for line in all_the_lines:
            line = line.replace(str(image_id), str(int(image_id) + 10000).zfill(6))
            line = line.replace("holothurian", "holothurian1")
            line = line.replace("echinus", "echinus1")
            line = line.replace("starfish", "starfish1")
            line = line.replace("scallop", "scallop1")
            f.write(line)
        f.close()

def convert_annotation2(image_id):
    #holothurian - echinus - starfish - scallop - holothurian
    in_file = '/home/xinzhichao/data/dataGAN/data/result/boxxml/%s.xml'%(image_id)
    xmls = glob.glob(in_file)
    for one_xml in xmls:
        print(one_xml)
        f = open(one_xml, 'r+', encoding='utf-8')
        all_the_lines = f.readlines()
        f.seek(0)
        f.truncate()
        for line in all_the_lines:
            line = line.replace("holothurian1", "echinus")
            line = line.replace("echinus1", "starfish")
            line = line.replace("starfish1", "scallop")
            line = line.replace("scallop1", "holothurian")
            f.write(line)
        f.close()
        new_name = '/home/xinzhichao/data/dataGAN/data/result/boxxml/' + str(int(image_id) + 10000).zfill(6) +'.xml' 
        os.rename(in_file, new_name)


#list_file_train = open('./trainlist1.txt').read().strip().split()     



def convert_annotation3(image_id):
    global num 
    num = num + 1
    in_file = '/home/xinzhichao/data/train_mix/addd/boxrename/%s.xml'%(image_id)
    xmls = glob.glob(in_file)
    for one_xml in xmls:
        print(one_xml)
        f = open(one_xml, 'r+', encoding='utf-8')
        all_the_lines = f.readlines()
        f.seek(0)
        f.truncate()
        for line in all_the_lines:
            line = line.replace(str(image_id),  'x'+str(num).zfill(6))
            f.write(line)
        f.close()
    new_name = '/home/xinzhichao/data/train_mix/addd/boxrename/' + 'x'+str(num).zfill(6) +'.xml' 
    os.rename(in_file, new_name)


list_file_train = open('./linshi.txt').read().strip().split()    



def image_convert(image_id):
    global num 
    num = num + 1
    in_file = '/home/xinzhichao/data/train_mix/addd/imagerename/%s.jpg'%(image_id)
    new_name = '/home/xinzhichao/data/train_mix/addd/imagerename/' +  'x'+str(int(num)).zfill(6) +'.jpg' 
    os.rename(in_file, new_name)

num = 0

for image_id in list_file_train:
    # list_file_train.write('/home/xinzhichao/Code/PyTorch-YOLOv3/data/customurpc/image/%s.jpg\n'%(image_id))  #应该是没啥用
    convert_annotation3(image_id)   
    #image_convert(image_id)
# from tqdm import tqdm

# path = "/home/xinzhichao/data/train_mix/addd/boxrename2" #文件夹目录
# files= os.listdir(path) #得到文件夹下的所有文件名称
# for file_name in tqdm(files): #遍历文件夹
#     convert_annotation3(file_name.split('.')[0])   
#     #image_convert(file_name.split('.')[0])