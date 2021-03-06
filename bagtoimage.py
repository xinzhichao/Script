# coding:utf-8
#!/usr/bin/python
 
# Extract images from a bag file.
 
#PKG = 'beginner_tutorials'
import roslib;   #roslib.load_manifest(PKG)
import rosbag
import rospy
import cv2
from sensor_msgs.msg import Image
from cv_bridge import CvBridge
from cv_bridge import CvBridgeError
 
# Reading bag filename from command line or roslaunch parameter.
#import os
#import sys
rgb = open('./rgb.txt','w')
depth = open('./depth.txt','w')


rgb_path = '/home/xinzhichao/Code3D/datakinect1/Color/Color'
depth_path= '/home/xinzhichao/Code3D/datakinect1/Depth/Depth'

class ImageCreator():
 

    def __init__(self):
        self.bridge = CvBridge()
        with rosbag.Bag('/home/xinzhichao/2020-12-26-20-04-21.bag', 'r') as bag:  #要读取的bag文件；
            for topic,msg,t in bag.read_messages():
                #print(t)
                if topic == "/camera/rgb/image_color": #图像的topic；

                        try:
                            cv_image = self.bridge.imgmsg_to_cv2(msg,"bgr8")
                        except CvBridgeError as e:
                            print e
                        timestr = "%.6f" %  msg.header.stamp.to_sec()
                        #%.6f表示小数点后带有6位，可根据精确度需要修改；
                        image_name = timestr+ ".png" #图像命名：时间戳.png
			#image_name = str(n)+ ".png" #图像命名：时间戳.png
                        rgb.write('\n'+str(timestr)+' '+'Color/'+'Color'+image_name)
                        cv2.imwrite(rgb_path + image_name, cv_image)  #保存；
                elif topic == "/camera/depth/image_raw": #图像的topic；

                        try:
                            cv_image = self.bridge.imgmsg_to_cv2(msg,"16UC1")
                        except CvBridgeError as e:
                            print e
                        timestr = "%.6f" %  msg.header.stamp.to_sec()
                        #%.6f表示小数点后带有6位，可根据精确度需要修改；
                        #image_name = str(m)+ ".png" #图像命名：时间戳.png
			image_name = timestr+ ".png"
			depth.write('\n'+str(timestr)+' '+'Depth/'+'Depth'+image_name)
                        cv2.imwrite(depth_path + image_name, cv_image)  #保存；
 
if __name__ == '__main__':
 
    #rospy.init_node(PKG)
 
    try:
        image_creator = ImageCreator()
    except rospy.ROSInterruptException:
        pass
