
import math
from math import modf
arrays=[0]*1001
arraysnum=[]
for i in range(1,1000):
    for j in range(1,1000):
        if i + j < 999:
            k = math.sqrt(pow(i,2)+pow(j,2))
            decimal, integer = modf(k)
            if decimal == 0:
                k = int(k)
                p = int(i + j + k)
                #print(p)
                if  p <= 1000:
                    #print(arrays[i + j + k])
                    if [p,j,i,k] not in arraysnum:
                        arraysnum.append([p,i,j,k])
                        arrays[p] += 1
                        #print("####################")
                        #print(arraysnum)
                        #print(arrays[i + j + k])
                        #print([p,i,j,k])
                        #print(p)
                        #    print(i + j + k)
        else:
            break
print (arrays.index(max(arrays)))