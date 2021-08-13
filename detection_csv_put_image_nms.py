import csv
import cv2
from tqdm import tqdm
import cv2
import numpy as np

def nms(bounding_boxes, confidence_score, threshold):
    if len(bounding_boxes) == 0:
        return [], []
    bboxes = np.array(bounding_boxes)
    score = np.array(confidence_score)

    # 计算 n 个候选框的面积大小
    x1 = bboxes[:, 0]
    y1 = bboxes[:, 1]
    x2 = bboxes[:, 2]
    y2 = bboxes[:, 3]
    areas =(x2 - x1 + 1) * (y2 - y1 + 1)

    # 对置信度进行排序, 获取排序后的下标序号, argsort 默认从小到大排序
    order = np.argsort(score)

    picked_boxes = [] # 返回值
    picked_score = [] # 返回值
    while order.size > 0:
        # 将当前置信度最大的框加入返回值列表中
        index = order[-1]
        picked_boxes.append(bounding_boxes[index])
        picked_score.append(confidence_score[index])
        # 获取当前置信度最大的候选框与其他任意候选框的相交面积
        x11 = np.maximum(x1[index], x1[order[:-1]])
        y11 = np.maximum(y1[index], y1[order[:-1]])
        x22 = np.minimum(x2[index], x2[order[:-1]])
        y22 = np.minimum(y2[index], y2[order[:-1]])
        w = np.maximum(0.0, x22 - x11 + 1)
        h = np.maximum(0.0, y22 - y11 + 1)
        intersection = w * h

        # 利用相交的面积和两个框自身的面积计算框的交并比, 将交并比大于阈值的框删除
        ratio = intersection / (areas[index] + areas[order[:-1]] - intersection)

        left = np.where(ratio > threshold)[0]
        #print(left)
        order = order[left]
        
    return picked_boxes, picked_score

with open('data.csv', 'r') as f:
    reader = csv.reader(f)
    result = list(reader)
    for j in range(820,1323):#1323
        image_path = "/home/xinzhichao/data2/slamdatasets/zhengziqiang/zheng0807/linshi/"+str("%05d" %j)+".png"
        save_path = "/home/xinzhichao/data2/slamdatasets/zhengziqiang/zheng0807/linshi2/"+str("%05d" %j)+".png"
        img = cv2.imread(image_path)
        confidence_score = []
        bounding_boxes = []
        for i in tqdm(range(1,36146)):
            if int(result[i][1]) ==j: 
                if result[i][0] == "echinus":
                    num_list = result[i][3:7]
                    num_list_new = [int(i) for i in num_list]#bbox框坐标
                    bounding_boxes = bounding_boxes + [num_list_new]
                    #print(bounding_boxes)
                    confidence_score = confidence_score + [float(result[i][2])]
                    #confidence_scores = [int(i) for i in confidence_score]
        #print(bounding_boxes)
        picked_boxes, picked_score=nms(bounding_boxes, confidence_score, threshold=0.9)
        print(picked_boxes)
        name = "sea urchin"
        for i in range(0, len(picked_boxes)):           
            cv2.rectangle(img, (int(picked_boxes[i][0]),int(picked_boxes[i][1])), (int(picked_boxes[i][2]),int(picked_boxes[i][3])), (0, 0, 255), 2)
                    #here
        if j <997:
            cv2.putText(img, name, (int(picked_boxes[i][0])-50,int(picked_boxes[i][1])-10), cv2.FONT_HERSHEY_COMPLEX_SMALL, 2, (0, 0, 255))
            cv2.putText(img, "  Id:1", (int(picked_boxes[i][0])+200,int(picked_boxes[i][1])-10), cv2.FONT_HERSHEY_COMPLEX_SMALL, 2, (0, 255, 0))
        elif j <1083:
            cv2.putText(img, name, (int(picked_boxes[i][0])-50,int(picked_boxes[i][1])-10), cv2.FONT_HERSHEY_COMPLEX_SMALL, 2, (0, 0, 255))
            cv2.putText(img, "  Id:2", (int(picked_boxes[i][0])+200,int(picked_boxes[i][1])-10), cv2.FONT_HERSHEY_COMPLEX_SMALL, 2, (0, 255, 0))
        elif j==1114:
            cv2.putText(img, name, (int(picked_boxes[i][0])-50,int(picked_boxes[i][1])-10), cv2.FONT_HERSHEY_COMPLEX_SMALL, 2, (0, 0, 255))
            cv2.putText(img, "  Id:1", (int(picked_boxes[i][0])+200,int(picked_boxes[i][1])-10), cv2.FONT_HERSHEY_COMPLEX_SMALL, 2, (0, 255, 0))
        elif j==1115:
            cv2.putText(img, name, (int(picked_boxes[i][0])-50,int(picked_boxes[i][1])-10), cv2.FONT_HERSHEY_COMPLEX_SMALL, 2, (0, 0, 255))
            cv2.putText(img, "  Id:1", (int(picked_boxes[i][0])+200,int(picked_boxes[i][1])-10), cv2.FONT_HERSHEY_COMPLEX_SMALL, 2, (0, 255, 0))
        elif j==1118:
            cv2.putText(img, name, (int(picked_boxes[i][0])-50,int(picked_boxes[i][1])-10), cv2.FONT_HERSHEY_COMPLEX_SMALL, 2, (0, 0, 255))
            cv2.putText(img, "  Id:1", (int(picked_boxes[i][0])+200,int(picked_boxes[i][1])-10), cv2.FONT_HERSHEY_COMPLEX_SMALL, 2, (0, 255, 0))
        elif j == 1121:
            cv2.putText(img, name, (int(picked_boxes[i][0])-50,int(picked_boxes[i][1])-10), cv2.FONT_HERSHEY_COMPLEX_SMALL, 2, (0, 0, 255))
            cv2.putText(img, "  Id:1", (int(picked_boxes[i][0])+200,int(picked_boxes[i][1])-10), cv2.FONT_HERSHEY_COMPLEX_SMALL, 2, (0, 255, 0))
        elif j==1130:
            cv2.putText(img, name, (int(picked_boxes[i][0])-50,int(picked_boxes[i][1])-10), cv2.FONT_HERSHEY_COMPLEX_SMALL, 2, (0, 0, 255))
            cv2.putText(img, "  Id:1", (int(picked_boxes[i][0])+200,int(picked_boxes[i][1])-10), cv2.FONT_HERSHEY_COMPLEX_SMALL, 2, (0, 255, 0))
        elif j ==1131:
            cv2.putText(img, name, (int(picked_boxes[i][0])-50,int(picked_boxes[i][1])-10), cv2.FONT_HERSHEY_COMPLEX_SMALL, 2, (0, 0, 255))
            cv2.putText(img, "  Id:1", (int(picked_boxes[i][0])+200,int(picked_boxes[i][1])-10), cv2.FONT_HERSHEY_COMPLEX_SMALL, 2, (0, 255, 0))
        elif j==1132:
            cv2.putText(img, name, (int(picked_boxes[i][0])-50,int(picked_boxes[i][1])-10), cv2.FONT_HERSHEY_COMPLEX_SMALL, 2, (0, 0, 255))
            cv2.putText(img, "  Id:1", (int(picked_boxes[i][0])+200,int(picked_boxes[i][1])-10), cv2.FONT_HERSHEY_COMPLEX_SMALL, 2, (0, 255, 0))
        elif  j==1133:
            cv2.putText(img, name, (int(picked_boxes[i][0])-50,int(picked_boxes[i][1])-10), cv2.FONT_HERSHEY_COMPLEX_SMALL, 2, (0, 0, 255))
            cv2.putText(img, "  Id:1", (int(picked_boxes[i][0])+200,int(picked_boxes[i][1])-10), cv2.FONT_HERSHEY_COMPLEX_SMALL, 2, (0, 255, 0))
        elif  j==1135:
            cv2.putText(img, name, (int(picked_boxes[i][0])-50,int(picked_boxes[i][1])-10), cv2.FONT_HERSHEY_COMPLEX_SMALL, 2, (0, 0, 255))
            cv2.putText(img, "  Id:1", (int(picked_boxes[i][0])+200,int(picked_boxes[i][1])-10), cv2.FONT_HERSHEY_COMPLEX_SMALL, 2, (0, 255, 0))
        elif  j==1140:
            cv2.putText(img, name, (int(picked_boxes[i][0])-50,int(picked_boxes[i][1])-10), cv2.FONT_HERSHEY_COMPLEX_SMALL, 2, (0, 0, 255))
            cv2.putText(img, "  Id:1", (int(picked_boxes[i][0])+200,int(picked_boxes[i][1])-10), cv2.FONT_HERSHEY_COMPLEX_SMALL, 2, (0, 255, 0))
        elif  j==1141:
            cv2.putText(img, name, (int(picked_boxes[i][0])-50,int(picked_boxes[i][1])-10), cv2.FONT_HERSHEY_COMPLEX_SMALL, 2, (0, 0, 255))
            cv2.putText(img, "  Id:1", (int(picked_boxes[i][0])+200,int(picked_boxes[i][1])-10), cv2.FONT_HERSHEY_COMPLEX_SMALL, 2, (0, 255, 0))
        elif  j==1142:
            cv2.putText(img, name, (int(picked_boxes[i][0])-50,int(picked_boxes[i][1])-10), cv2.FONT_HERSHEY_COMPLEX_SMALL, 2, (0, 0, 255))
            cv2.putText(img, "  Id:1", (int(picked_boxes[i][0])+200,int(picked_boxes[i][1])-10), cv2.FONT_HERSHEY_COMPLEX_SMALL, 2, (0, 255, 0))
        elif  j==1146:
            cv2.putText(img, name, (int(picked_boxes[i][0])-50,int(picked_boxes[i][1])-10), cv2.FONT_HERSHEY_COMPLEX_SMALL, 2, (0, 0, 255))
            cv2.putText(img, "  Id:1", (int(picked_boxes[i][0])+200,int(picked_boxes[i][1])-10), cv2.FONT_HERSHEY_COMPLEX_SMALL, 2, (0, 255, 0))
        elif j==1147:
            cv2.putText(img, name, (int(picked_boxes[i][0])-50,int(picked_boxes[i][1])-10), cv2.FONT_HERSHEY_COMPLEX_SMALL, 2, (0, 0, 255))
            cv2.putText(img, "  Id:1", (int(picked_boxes[i][0])+200,int(picked_boxes[i][1])-10), cv2.FONT_HERSHEY_COMPLEX_SMALL, 2, (0, 255, 0))
        elif  j==1148:
            cv2.putText(img, name, (int(picked_boxes[i][0])-50,int(picked_boxes[i][1])-10), cv2.FONT_HERSHEY_COMPLEX_SMALL, 2, (0, 0, 255))
            cv2.putText(img, "  Id:1", (int(picked_boxes[i][0])+200,int(picked_boxes[i][1])-10), cv2.FONT_HERSHEY_COMPLEX_SMALL, 2, (0, 255, 0))
        elif  j==1149:
            cv2.putText(img, name, (int(picked_boxes[i][0])-50,int(picked_boxes[i][1])-10), cv2.FONT_HERSHEY_COMPLEX_SMALL, 2, (0, 0, 255))
            cv2.putText(img, "  Id:1", (int(picked_boxes[i][0])+200,int(picked_boxes[i][1])-10), cv2.FONT_HERSHEY_COMPLEX_SMALL, 2, (0, 255, 0))
        elif  j==1150:
            cv2.putText(img, name, (int(picked_boxes[i][0])-50,int(picked_boxes[i][1])-10), cv2.FONT_HERSHEY_COMPLEX_SMALL, 2, (0, 0, 255))
            cv2.putText(img, "  Id:1", (int(picked_boxes[i][0])+200,int(picked_boxes[i][1])-10), cv2.FONT_HERSHEY_COMPLEX_SMALL, 2, (0, 255, 0))
        elif  j==1151:
            cv2.putText(img, name, (int(picked_boxes[i][0])-50,int(picked_boxes[i][1])-10), cv2.FONT_HERSHEY_COMPLEX_SMALL, 2, (0, 0, 255))
            cv2.putText(img, "  Id:1", (int(picked_boxes[i][0])+200,int(picked_boxes[i][1])-10), cv2.FONT_HERSHEY_COMPLEX_SMALL, 2, (0, 255, 0))
        else:
            cv2.putText(img, name, (int(picked_boxes[i][0])-50,int(picked_boxes[i][1])-10), cv2.FONT_HERSHEY_COMPLEX_SMALL, 2, (0, 0, 255))
            cv2.putText(img, "  Id:3", (int(picked_boxes[i][0])+200,int(picked_boxes[i][1])-10), cv2.FONT_HERSHEY_COMPLEX_SMALL, 2, (0, 255, 0))
                #img = img
        cv2.imwrite(save_path, img)



