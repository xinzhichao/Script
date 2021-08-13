import matplotlib.pyplot as plt
import numpy as np
import scipy.misc
import os
from tqdm import tqdm
import glob
file_dir = "/home/xinzhichao/data2/monodepth/ACAN/datasets/underwater/npy1/"  # npy文件路径
dest_dir = "/home/xinzhichao/data2/monodepth/ACAN/datasets/underwater/npy2/"  # 文件存储的路径


def npy_png(file_dir, dest_dir):
    # 如果不存在对应文件，则创建对应文件
    if not os.path.exists(file_dir):
        os.makedirs(file_dir)
    if not os.path.exists(dest_dir):
        os.makedirs(dest_dir)
    path = sorted(glob.glob(file_dir+"/*.npy" ))
    for npypath in tqdm(path):
        npypath = npypath.split("/")[-1]
        #print(npypath)
        files = file_dir +npypath  # npy文件
        con_arr = np.load(files)  # 读取npy文件
#352
        disp_to_img = scipy.misc.imresize(con_arr, [352, 640])  # 根据需要的尺寸进行修改h w
        savepngname = npypath.split(".")[0]
        #plt.imsave(os.path.join(dest_dir, "{}.png".format(savepngname)), con_arr, cmap='gray')  # 定义命名规则，保存图片为彩色模式
        save_full_path = os.path.join(dest_dir, "{}.png".format(savepngname))
        #scipy.misc.imsave(save_full_path, con_arr)
        #print('photo {} finished'.format(i))

        plt.imsave(save_full_path, disp_to_img, cmap="plasma")

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

def resizeimage():
    input_path = "/home/xinzhichao/data2/monodepth/ACAN/datasets/underwater/rgbbeforea/" #背景图像路径
    output_path =  "/home/xinzhichao/data2/monodepth/ACAN/datasets/underwater/rgbbefore/" 
    files_im= os.listdir(input_path)#得到文件夹下的所有文件名称
    #files_im.sort(key=lambda x:int(x.split('.')[0].split('x')[1]))

    #change_imagename() #修改图像文件名,之前文件夹中图像文件名的命名方式是类别加数字，更改后是纯数字命名
    for file_name in tqdm(files_im): #遍历文件夹
        image =  cv2.imread(input_path + str(file_name))

        image = cv2.resize(image, (640, 480))
        cv2.imwrite(output_path+ str(file_name) , image)




from PIL import Image

def print_imageinfo():
    img = Image.open("/home/xinzhichao/data2/monodepth/ACAN/datasets/underwater/1.png")
    # img.show()

    print(img.size)#获取图片大小（width， height）
    print(img.size[0], img.size[1]) #（width， height）
    print(img.mode)#获取图片模式{'1':1, 'L':8, 'P':8(带颜色表), 'RGB':24, 'RGBA':32,}
    print(img.format)
    print(img.info) #打印的信息类似下方注释，当然必须图片内部包含该信息才行

    img = np.array(img)
    print("image_array: ", img.shape)

    # sequ = img.getdata()
    # sequ0 = list(sequ)
    # #print(sequ0)#获取图片像素值

    # if img.mode == 'P':
    #     print(img.palette.palette)#打印颜色表
    #     # lut = img.resize((99, 99))
    #     # lut.putdata(range(256))
    #     lut = lut.convert("RGB")#将图片转换为RGB图像
    #     #print(list(lut.getdata()))#打印图像RGB像素值
    #     # pix = lut.load()
    #     # print(pix[1, 0])
    #     # lut.show()
    #     # lut now contains a sequence of (r, g, b) tuples

    # #pix = img.load()
    # #print(pix[img.size[0]/2, img.size[1]/2])#某个点（x, y）的像素值

    # if img.mode == 'RGBA':
    #     r,g,b, a = img.split()
    #     print(r.mode)
    #     print(r.size)
    #     print(img.size)




if __name__ == "__main__":
    npy_png(file_dir, dest_dir)
    #resizeimage()
    #print_imageinfo()
