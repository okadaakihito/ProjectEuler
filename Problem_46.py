import math
imax=100000
arrays=[2]
karrays=[]
for i in range(3,imax,2):
    flag=1
    maxn=int(math.sqrt(i))
    for r in range(3,maxn+1,2):
        if i % r == 0 :
            flag = 0
            break
    if flag == 1 :
        arrays.append(i)
    else :
        karrays.append(i)
for i in range(0,imax):
    for j in range(1,imax):
        flag = 0
        k = karrays[i] - 2 * math.pow(j,2)
        if k not in arrays:
            if k < 0:
                flag = 1
                break
        else:
            break
    if flag == 1:
        break
print(karrays[i])