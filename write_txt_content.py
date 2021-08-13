import os

f = open('./habr.txt','w')
for i in range(817,1329):
	#f.write('\n'+"frame"+str("%06d" %i)+'.png')
	f.write('\n'+str("%05d" %i)+'.png')
