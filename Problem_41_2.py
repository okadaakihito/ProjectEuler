import math
import itertools
imax = 9
while True:
    arrays = []
    for i in range(imax,0,-1):
        arrays.append(i)
    lists = list(itertools.permutations(arrays))
    length=len(lists)
    for j in range(0,length):
        iss=''
        if lists[j][imax-1] % 2 != 0 :
            for k in range(0,imax):
                iss=iss+str(lists[j][k])
            ii=int(iss)
            maxn=int(math.sqrt(ii))
            flag=1
            for r in range(3,maxn+1,2):
                if ii % r == 0 :
                    flag = 0
                    break
            if flag == 1 :
                print("####")
                print(ii)
                break
    imax = imax - 1
    if flag == 1 :
        break
#7652413
