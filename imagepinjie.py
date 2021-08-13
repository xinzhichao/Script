import cv2
import glob
import numpy as np
from tqdm import tqdm
#将生成的图片进行分类裁剪并且将图像恢复到原始图像大小

# right_path = "/home/xinzhichao/data/slamdatasets/media/results_image/frame000001.png"
# img_right = cv2.imread(right_path)
# #拼接后图像
# img_result = cv2.resize(img_right, (640, 352))
# img_left = img_result
# img_right = img_result
path = sorted(glob.glob("/home/xinzhichao/data/slamdatasets/media/results_image/*.png" ))
for pathname in tqdm(path):
    print(pathname)
    img_org = cv2.imread(pathname)
    #左侧图像读取
    img_left = img_org[0:352 , 0:640]
    #右侧图像读取
    img_right = img_org[0:352 , 640:1280]
    # #拼接后图像
    result_name = pathname.split("/")[-1]
    cv2.imwrite("/home/xinzhichao/data/slamdatasets/media/result_left/" + str(result_name) , img_left)
    cv2.imwrite("/home/xinzhichao/data/slamdatasets/media/result_right/" + str(result_name) , img_right)






