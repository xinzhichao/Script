

import os
path="/home/xinzhichao/Code3D/datakinect1/Color/"       
f = open('./rgb.txt','w')

fileList=os.listdir(path)

n=0
for i in fileList:
    oldname=path+ os.sep + fileList[n]  
    f.write('\n'+str(i)+' '+'Color/'+str(oldname))
    n+=1
