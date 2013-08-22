import math
def create_pns(x, y):
    #parrays=[ i for i in range(x,y,2) for r in range(3,maxn+1,2) if i % r == 0 ]
    parrays=[2]
    for i in range(x,y,2):
        flag=1
        for r in range(3,maxn(i)+1,2):
            if i % r == 0:
                flag = 0
                break
        if flag == 1 :
            parrays.append(i)
    return parrays

def maxn(i):
    maxn=int(math.sqrt(i))
    return maxn