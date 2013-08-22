import math
imax=1000000
arrays=[2]
countmax=4
maxval=[0,0,2,6,30]
maxjud=[0,0,10,10,10]
for i in range(3,imax,2):
    flag=1
    maxn=int(math.sqrt(i))
    for r in range(3,maxn+1,2):
        if i % r == 0 :
            flag = 0
            break
    if flag == 1 :
        arrays.append(i)
for i in range(10,imax):
    if( i == 1 #
         or flag != 3 ):
        lasti=i
        count=0
    iss=i
    flag=1
    rmax=int(i/maxval[countmax])
    sarrays=[]
    for r in range(2,rmax):
        while iss % r == 0 :
            flag = 0
            iss = iss / r
            if r not in sarrays:
                sarrays.append(r)
            if r not in arrays:
                flag = 1
                break
        if (maxjud[countmax] < r #
            and flag == 1):
            flag = 1
            break
    #print(iss)
    #print(flag)
    if ( flag == 0 #
        and iss == 1
        and (i == lasti
             or (i-1) == lasti)
        and len(sarrays) == countmax ):
        #print(i)
        #print(sarrays)
        lasti=i
        count=count+1
        flag=3
        if count == countmax :
            break
print(lasti-countmax+1)
