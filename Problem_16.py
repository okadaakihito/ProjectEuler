# -*- coding: utf-8 -*-
print ("Start")
#初期値の代入
y=1
sumdig=0
for i in range(0,1000):
        y=2*y
ylen=int(len(str(y)))
stry=str(y)
for j in range(0,ylen):
    strdig = int (stry[j:j+1])
    sumdig=strdig+sumdig
print ("Len is " + str(ylen))
print ("Power digit sum is " + str(sumdig))
print ("End")